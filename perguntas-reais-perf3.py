import openai

# alberto
openai.api_key = 1

##########################
#### PERGUNTA PERF 1 #### 
##########################

pergunta="""
Suponha que você é um especialista em testes de carga e estresse, usando jMeter em Java.

Você é capaz de planejar e executar testes de carga e estresse com jMeter em aplicações que expõe APIs REST para avaliar o desempenho, escalabilidade e resiliência destas aplicações a fim de identificar gargalos de performance.

Além de especialista, você corrige provas sobre o tópico. 

Considere a seguinte pergunta e a seguinte resposta:

P: Quais são as principais métricas utilizadas para avaliar o desempenho de uma aplicação durante um teste de carga?
R: {}

Qual nota você daria para esta resposta, numa escala de 0 a 10? Pense passo a passo.

Devolva a resposta em um formato JSON, com uma variável 'nota', com a sua nota, e uma outra variável 'explicação', com a explicação para esta nota. 

Sua explicação deve ter ao menos 20 palavras. Escreva a resposta usando UTF-8. Se nenhuma resposta for informada, informe que 'Nenhuma resposta foi informada', e de nota zero.
"""

resposta1 = """
'- Simular as diversas jornadas do cliente
- Se possivel realizar os testes em ambiente produtivo em horarios de baixassima utilizacao
"""
resposta2 = """
A ideia é o sistema em questão esteja preparado para receber o quantidade de carga massiva, o aumento de carga vai acontecendo de forma crescente ao longo de um determinado tempo, monitorar as métricas de infraestura, da aplicação e status code devolvido (não testar as diferentes resposta e payload retornado, mas sim se a aplicação fica indisponível).
"""
resposta3 = """
Testar a carga com base nas premissas de negócio em um ambiente igual ou muito similar ao de produção. Coletar as métricas e avaliar potenciais gargalos que a aplicação pode ter.
"""
resposta4 = """
Para teste de carga é bom ir incrementando aos poucos o volume de demanda simultanea à API visando encontrar qual seria o volume atual atendido pela API. E a partir daí poderia ser trabalhado como aumentar este volume.
Outra prática é teste de fluxo. Podemos fazer o teste de carga em um único endpoint (talvez o que precise ter mais resiliencia) ou até mesmo um teste de carga em fluxo. Colocando uma sequencia de chamadas ao sistema, simulando usuários virtuais interagindo com as API em uma sequencia lógica de fluxo. Desta forma, alguns usuários podem até estar em pontos diferentes do fluxo em um mesmo instante.
"""
resposta5 = """
"""
resposta6 = """
não sei
"""
resposta7 = """
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
