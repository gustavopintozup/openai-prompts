import pandas as pd
import openai, os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('KEY')

import warnings

# Desabilitar a impressão de todos os warnings
warnings.filterwarnings("ignore")

template="""
Eu preciso que você realize correções de provas usando a régua de correção mais alta que você puder.

Considere a seguinte pergunta e a seguinte resposta de um especialista:

P: {}
R especialista: {}

Agora, considere a resposta de um aluno, fornecida abaixo.

R aluno: {}

Qual nota você daria para a resposta do aluno, levando em consideração a resposta do especialista, numa escala de 0 a 10? 

Devolva a resposta em um formato JSON, com uma variável 'nota', com a sua nota, e uma outra variável 'explicacao' com a explicação para esta nota. Sua explicação deve ter ao menos 20 palavras. Na explicação, identifique lacunas de conhecimento e explique de forma que minimize essa lacuna, utilizando exemplos reais.

Se nenhuma resposta for informada, informe que 'Nenhuma resposta foi informada', e de nota zero.
"""

pergunta_cache_1 = "Explique com suas palavras o que você entende sobre caching de aplicações REST?"
reference_cache_1 = "Caching é uma técnica que permite armazenar dados que são acessados frequentemente em memoria, afim de reduzir o custo de complexidade da consulta dos mesmos. Hoje em dia existem diversas formas de aplicar caching em REST APIs, iniciando ao lado do servidor através de técnincas de cache local e distruido. E também é possível habilitar o caching ao lado cliente, onde através do uso de cabecalhos do protocolo HTTP, é definido politicas que regem o comportamento do caching, como por exemplo, o uso de versões, tempo de expiração e também definir quais clientes podem armazenar os dados, no caso referindo ao navegador do usuario final e/ou CDNs."

pergunta_cache_2 = "Explique brevemente o funcionamento dos dois tipos de caching: caching do lado do cliente e caching do lado do servidor."
reference_cache_2 = "Cache ao lado do servidor pode ser servido, de forma local, fazendo com que um espaço no heap de memoria do servidor seja utilizado para armazenar dados que tem alto custo de rede ou computação, e que são acessados com alta frequência. Esta estratégia deve ser utilizada em cénarios onde a arquitetura do sistema seja monolitica ou exista a restrição que apenas uma instância do sistema seja utilizado. Outra forma de prover cache na camada de aplicação é através do uso de provedores de cache distribuido, favorecendo que um ponto global de acesso seja compartilhado entre as instâncias, facilitando que os dados estejam sincronizados com a fonte da verdade."

pergunta_cache_3 = "Explique o invalidação de cache em aplicações REST e apresente uma forma de resolve-lo."
reference_cache_3 = "Invalidação em cache é uma operação que visa manter o caching enxuto e consistente, e para oferecer essas garantias, deve ser utilizados politicas de invalidação, alguns exemplos são Least Recently Used (LRU) que visa remover do caching os dados que não são foram acessados recentemente. Outro exemplo de politica é a Least Frequently Used (LFU) que visa remover do caching os dados que são menos acessados. Também existem provedores que trabalham com politicas de expiração, onde os dados entram com um tempo de duração, ao atingir determinado o tempo são automaticamente removidos do cache."

pergunta_perf_1 = "Explique o conceito de teste de carga e estresse?"
reference_perf_1 = "Teste carga signigica verificar como uma aplicação ou sistema se comporta sob uma determinada carga de trabalho (workload) esperada, que pode ser uma carga pequena, moderada ou grande. Além disso, essa carga é aplicada durante algum intervalo de tempo, como minutos ou horas, para validar a estabilidade do sistema e detectar possíveis problemas no uso de recursos, como memória, CPU, disco ou conexões com um banco de dados por exemplo. É importante entender que um teste de carga não ultrapassa a capacidade esperada ou projetada para uma aplicação ou sistema. Enquanto teste de estresse está relacionado a verificar como uma aplicação ou sistema se comporta quando aplicamos uma carga de trabalho (workload) muito alta e intensa, geralmente uma carga superior a esperada ou especificada nos requisitos. A ideia aqui é submeter a aplicação além da sua capacidade projetada a fim de detectar problemas ou gargalos no uso de recursos ou componentes internos. O objetivo é descobrir como o sistema se comporta sob pressão extrema, como picos de tráfego, uso excessivo de recursos, falhas de hardware ou condições anormais."

pergunta_perf_2 = "Quais são as principais métricas utilizadas para avaliar o desempenho de uma aplicação durante um teste de carga?"
reference_perf_2 = "Geralmente numa aplicação web, incluindo APIs REST, as principais métricas que coletamos e avaliamos são: response time (tempo de resposta), throughput (quantidade de operações por unidade de tempo) e error rate (taxa de erros). Tanto é que existe um método bastante conhecido como 'RED Method', que basicamente recomenda avaliarmos estas 3 métricas para aplicações e serviços orientados a requisições (request-based services). Para aplicações não orientadas a requisições, como batch processing ou serviços de streaming por exemplo, costuma-se também coletar e avaliar outras métricas como CPU, memória ou rede."

pergunta_perf_3 = "Quais são as melhores práticas para realizar testes de carga em aplicações que expõem APIs REST?"
reference_perf_3 = """
Existem diversos práticas importantes na hora de realizar testes de carga, como definir os casos de uso a se validar e as expectativas da carga de trabalho (workload) esperada. Também é importante definir quais métricas são relevantes para o teste, afinal, serão elas que ajudarão a identificar problemas e gargalos de performance (aqui o "RED Method" pode ser adotado). Outro pronto é rodar os testes de carga contra uma aplicação em produção ou com ambiente parecido ao ambiente da produção, como um ambiente de homologação, dessa forma teremos números próximos da realidade do sistema. E não menos importante, aplicar os testes com uma massa de dados realista sempre que possível.
"""

perguntas = [pergunta_cache_1, pergunta_cache_2, pergunta_cache_3,
             pergunta_perf_1, pergunta_perf_2, pergunta_perf_3]

respostas_specs = [reference_cache_1, reference_cache_2, reference_cache_3,
                       reference_perf_1, reference_perf_2, reference_perf_3]

def calcular_nota_gpt(prompt):
    messages=[{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=200,
        temperature=1.2,
        messages = messages)

    return response['choices'][0]["message"]


def calcular_bleu(reference, resposta):
    from nltk.translate.bleu_score import sentence_bleu

    return sentence_bleu(reference, resposta)


def calcular_cos_sim(reference, resposta):
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Two lists of sentences
    sentences1 = [resposta]
    sentences2 = [reference]

    #Compute embedding for both lists
    embeddings1 = model.encode(sentences1, convert_to_tensor=True)
    embeddings2 = model.encode(sentences2, convert_to_tensor=True)

    #Compute cosine-similarities
    cosine_scores = util.cos_sim(embeddings1, embeddings2)

    #Output the pairs with their score
    for i in range(len(sentences1)):
        return "{:.4f}".format(cosine_scores[i][i])


def calcular_respostas(prompt_template):
    id_pergunta = 5

    respostas = pd.read_csv("responses-nao-completaram-treino.csv")
    respostas = respostas.iloc[:, id_pergunta+1].values

    for resposta in respostas:
        try:

            pergunta = perguntas[id_pergunta]
            resposta_spec = respostas_specs[id_pergunta]
            resposta_aluno = ''.join(resposta.splitlines())

            prompt = prompt_template.format(pergunta, resposta_spec, resposta_aluno)

            gpt = calcular_nota_gpt(prompt)
            
            import json
            gpt_explicacao = json.loads(gpt["content"])

            bleu = calcular_bleu(reference_perf_1, resposta_aluno)
            cos = calcular_cos_sim(reference_perf_1, resposta_aluno)
            print("{}; {}; {}; {}; {}".format(resposta_aluno.replace(";", "."), 
                                              gpt_explicacao["nota"], 
                                              gpt_explicacao["explicacao"], 
                                              bleu, cos))
        except:
            print("NA; 0; NA; 0; 0")

"""
def calcular_respostas_spec(prompt):
    id_pergunta = 5
    resposta = resposta_referencia[id_pergunta]
    
    try:
        prompt = prompt.format(perguntas[id_pergunta], resposta)
        
        gpt = calcular_nota_gpt(prompt)
        
        import json
        gpt_explicacao = json.loads(gpt["content"])

        print("{}; {}; {};".format(resposta, gpt_explicacao["nota"], gpt_explicacao["explicacao"]))
    except:
        print("NA; 0; NA; 0; 0")
"""


calcular_respostas(template)