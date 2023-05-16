import openai

# alberto
openai.api_key = 1

##########################
#### PERGUNTA CACHE 1 #### 
##########################

pergunta="""
Suponha que você é um especialista em testes de carga e estresse, usando jMeter em Java.

Você é capaz de planejar e executar testes de carga e estresse com jMeter em aplicações que expõe APIs REST para avaliar o desempenho, escalabilidade e resiliência destas aplicações a fim de identificar gargalos de performance.

Além de especialista, você corrige provas sobre o tópico. 

Considere a seguinte pergunta e a seguinte resposta:

P: Explique brevemente o funcionamento dos dois tipos de caching:  caching do lado do cliente e caching do lado do servidor.
R: {}

Qual nota você daria para esta resposta, numa escala de 0 a 10? Pense passo a passo.

Devolva a resposta em um formato JSON, com uma variável 'nota', com a sua nota, e uma outra variável 'explicação', com a explicação para esta nota. 

Sua explicação deve ter ao menos 20 palavras. Escreva a resposta usando UTF-8. Se nenhuma resposta for informada, informe que 'Nenhuma resposta foi informada', e de nota zero.
"""

reposta1 = """
Do lado do cliente eh possivel armazenar dados eh arquivos como imagens e arquivos responsaveis pelo design da interface grafica, aumentando a velocidade de exibicao de telas para o cliente (tanto web como mobile) evitando que a todo requisicao essas informacoes que nao mudam com frequencia sejam fornecidas pelo servidor da aplicacao.
Do lado do ser do servidor, requisicoes que nao alteram com muita frequencia e que sao compartilhadas por diversos usuarios podem ser armazenadas em cache, evitando que a requisicao chegue ate a camada da aplicacao e posteriormente na camada de dados (banco-de-dados), liberando esses recursos para atenderem requisicoes (statefull) que nao podem ser cacheadas.
"""
resposta2 = """
Caching do lado do cliente é utilizado para que ele tenha acesso mais rápido a certos recursos (como o cache do navegador) e é individual para cada cliente. Caching do lado do servidor irá manter em cache recursos do servidor para se ter acesso mais rápido a esses recursos, com a diferença que todos os clientes que acessarem este servidor irão receber a mesma informação de cache.
"""
resposta3 = """
O Caching do lado do cliente, é quando o cliente "evita" fazer uma request, pois nas requests prévias ele recebeu uma sinalização que pode armazenar temporariamente. No lado do servidor, significa que deliberadamente quem desenvolveu uma funcionalidade, entende que algum processamento é repetitivo (como o rendering de uma página html, ou uma listagem de uma API Rest), e pode armazenar seu resultado em memória, fazendo com que o tempo de resposta diminua e também o uso de CPU.
"""
resposta4 = """
Caching do lado do cliente seria menos genérico, mais focado na linha de processamento do cliente, a ideia seria evitar multiplas chamadas idênticas ao servidor em um curto espaço de tempo. A primeira chamada ficaria cacheada, e ao tentar realizar a segunda chamada, o modulo de cache identifica que já existe uma resposta armazenada e não chamaria o serviço.
Ja o cache do lado do servidor, teria uma lógica mais aberta, focada em processamento do servidor, cacheando respostas de sub-processamentos internos (dado os mesmos parâmetros, se a resposta é pouco mutável, poderia ser cacheado) ou até mesmo cacheando respostas da sua propria API.
"""
resposta5 = """
"""
resposta6 = """
caching do lado do cliente, as informações sao armazenadas do lado cliente, porem se outro cliente tentar obter a mesma informação, o servidor ira processar.  Já do lado do servidor, vários clientes podem chamar porém o servidor terá a informação ja armazenada após uma primeira execução
"""
resposta7 = """
Do lado do servidor é cachear do lado da aplicação do servidor ( backend ).
"""

respostas = [reposta1, resposta2, resposta3, resposta4, resposta5, resposta6, resposta7]

# models
# gpt-3.5-turbo-0301
# gpt-4
# davinci
# https://platform.openai.com/docs/models/


for resposta in respostas:
    messages=[{"role": "user", "content": pergunta.format(resposta)}]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=100,
        temperature=1.2,
        messages = messages)

    print(response['choices'][0]["message"])
