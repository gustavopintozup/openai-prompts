import openai

# alberto
openai.api_key = 1

##########################
#### PERGUNTA PERF 1 #### 
##########################

pergunta="""
Você consegue simular a atuação de um professor de universidade Ivy League, especializado em caching e testes de carga e stress? Eu preciso que você realize correções de provas usando a régua de correção mais alta que você puder.

Considere a seguinte pergunta e a seguinte resposta:

P: Quais são as principais métricas utilizadas para avaliar o desempenho de uma aplicação durante um teste de carga?
R: {}

Qual nota você daria para esta resposta, numa escala de 0 a 10? Pense passo a passo.

Devolva a resposta em um formato JSON, com uma variável 'nota', com a sua nota, e uma outra variável 'explicação', com a explicação para esta nota. 

Sua explicação deve ter ao menos 20 palavras. Escreva a resposta usando UTF-8. Se nenhuma resposta for informada, informe que 'Nenhuma resposta foi informada', e de nota zero.
"""

resposta1 = """
'- Qtd de requisicoes simultaneas por segundo
- Tempo de resposta das requisicoes (percentile, media)
- Escabilidade de infrastrutura
"""
resposta2 = """
Tempo de resposta, métricas de infraestrutura, quantidade de transações por segundo (TPS), status code devolvido, etc
"""
resposta3 = """
Requisições por segundo, ou Transações por segundo, ou mensagens processadas por segundo, percentual de uso de CPU, percentual de uso de memória e percentual de utilização de I/O
"""
resposta4 = """
As metricas mais utilizadas são tempo de resposta, resiliencia, capacidade de auto-scaling quando atingir os limites ou até mesmo, caso ocorra um crash, o tempo de recover para a aplicação voltar a atender a demanda.
"""
resposta5 = """
"""
resposta6 = """
tempo de resposta, quantidade de erros
"""
resposta7 = """
'- QUANTIDADE DE USUÁRIO
- QUANTIDADE DE REQUISIÇÕES
- TEMPO DESSAS CHAMADAS
"""

respostas = [resposta1, resposta2, resposta3, resposta4, resposta5, resposta6, resposta7]

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


