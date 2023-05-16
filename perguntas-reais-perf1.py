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

P: Explique o conceito de teste de carga e estresse?
R: {}

Qual nota você daria para esta resposta, numa escala de 0 a 10? Pense passo a passo.

Devolva a resposta em um formato JSON, com uma variável 'nota', com a sua nota, e uma outra variável 'explicação', com a explicação para esta nota. 

Sua explicação deve ter ao menos 20 palavras. Escreva a resposta usando UTF-8. Se nenhuma resposta for informada, informe que 'Nenhuma resposta foi informada', e de nota zero.
"""

reposta1 = """
A ideia testar a aplicacao em ambiente controlado simulando cenarios de extrema concorrencia, ou seja, realizar milhares requisicoes simultaneas a aplicacao com o objetivo de observar como ela ira se comportar e capturar o resultados do teste para aplicar melhorias que se fizerem necessarias (tanto na aplicacao como na infrastrutura) deixando a aplicacao preparada para suportar altas cargas em ambiente produtivo.
"""
resposta2 = """
O teste de carga tem como objetivo testar os limites do que for o objetivo dele, enquanto o de estresse tem o objetivo de estressar o sistema para ver cenários de crash, etc.
"""
resposta3 = """
Um teste de carga coloca uma carga de trabalho esperada em uma peça, para ver se ela atende às expectativas, ex: 100 requisições por segundo num endpoint rest. Um teste de estresse é semelhante, mas ele adiciona carga até um ponto de ruptura.
"""
resposta4 = """
Teste de carga ou estresse são tecnicas utilizadas para avaliar a resiliencia, desempenho da aplicação quando encontrado uma solução acima do normal/esperado. Onde submetemos o sistema/API a uma demanda mais extrema, a fim de identificarmos os gargalos (bottlenecks) ou até mesmo os limites que o sistema suportaria.
"""
resposta5 = """
"""
resposta6 = """
Teste de carga valida se a aplicação mantem o desempenho mesmo com um aumento esperado da quantidade de usuarios simultaneos  

Teste de stresse valida até quantos usuarios simultaneos efetuando requisições a aplicação aguenta
"""
resposta7 = """
E um teste para verificar o desempenho e tempo de respostas com várias requisições em uma API REST. Com o resultado pode-se definir em que pontos colocar cache e também outras decisões para resolver o problema (caso tenha)
"""

respostas = [resposta5, resposta6, resposta7]

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
