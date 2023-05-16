import openai

# alberto
openai.api_key = 111

##########################
#### PERGUNTA CACHE 1 #### 
##########################

pergunta="""
Suponha que você é um especialista em testes de carga e estresse, usando jMeter em Java.

Você é capaz de planejar e executar testes de carga e estresse com jMeter em aplicações que expõe APIs REST para avaliar o desempenho, escalabilidade e resiliência destas aplicações a fim de identificar gargalos de performance.

Além de especialista, você corrige provas sobre o tópico. 

Considere a seguinte pergunta e a seguinte resposta:

P: Explique com suas palavras o que você entende sobre caching de aplicações REST?
R: {}

Qual nota você daria para esta resposta, numa escala de 0 a 10? Pense passo a passo.

Devolva a resposta em um formato JSON, com uma variável 'nota', com a sua nota, e uma outra variável 'explicação', com a explicação para esta nota. 

Sua explicação deve ter ao menos 20 palavras. Escreva a resposta usando UTF-8. Se nenhuma resposta for informada, informe que 'Nenhuma resposta foi informada', e de nota zero.
"""

reposta1 = """
Estrategia utilizada com objetivo de ganho de performance de uma aplicacao. Como explicado na introducao do questionario, armazenando respostas de requisicoes REST na aplicacao cliente ou do lado do servidor.
O conceito eh simples mas sua aplicacao requer uma analise do que pode ou nao ser armazenado em cache.
Dados de requisicoes stateless sao principais candidatos e serem armazenados em cache, como exemplo o catalogo de produtos de um e-commerce, que eh compartilhada pelos usuarios do sistema.
Ha casos de requisicoes stateless que necessitem de dados atuais e concistentes (exemplo: extrato bancario) onde o uso de caching eh arriscado, pois existe a possibilidade da informacao estar desatualizada (stale).
O caching traz ganho tanto para responsividade como tambem a carga de processamento no lado do servidor (economia de infra).
"""
resposta2 = """
Entendo que caching tem que ser utilizado levando em conta certas condições como se aquela informação em cache não fica alternando durante o tempo estipulado para o cache; cache sempre bom ter uma expiração, pois uma vez certa informação atualizado em alguma base, fica desatualizado no cache; o cache fica disponível na memoria RAM o que possibilita um retorno mais rápido, mas também é uma memória mais cara e limitada em tamanho (comparado ao armazenamento secundário).
"""
resposta3 = """
O mecanismo de cache consiste em a aplicação identificar no response se o resultado de uma requisição pode ser armazenado temporariamente e por quanto tempo, a fim de diminuir a quantidade de solicitações. Dessa forma o cliente http ou servidores intermediários, conseguem armazenar temporariamente a resposta diminuindo a carga do servidor original, dessa forma, atendendo "virtualmente" mais requisições.
"""
resposta4 = """
Vejo 2 modelos de caching. Caching do servidor e Caching do cliente. No servidor, seria para evitar reprocessamento de informações que são pouco mutáveis, procurando gerar uma resposta mais rápida ao cliente. Ex: Caching de configurações, rotas, permissões de uma role, etc.
Já o caching do lado do cliente, seria para evitar chamadas ao servidor, utilizado muito para chamadas de serviços de busca, onde dado o mesmo filter/query o resultado seria o mesmo. Ex: Caching de consulta dos serviços de CEP, caching das permissões do usuário para ser utilizado no client
"""
resposta5 = """
"""
resposta6 = """
São informaçoes pré-armazenadas após uma primeira execução da API e que quando essa mesma API é chamada novamente com os mesmos dados de entrada, essas informações são resgatadas sem que hava algum tipo de processamento pelo microserviço
"""
resposta7 = """
Caching entendo como uma forma de diminuir o processamento que não muda o estado do dado. Geralmente usa em metodos GET para não usar muitos recurso e desafogar a aplicação ou até mesmo evitar erros de integração com outras APIs
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
