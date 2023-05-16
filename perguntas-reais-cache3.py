import openai

# alberto
openai.api_key = 1

##########################
#### PERGUNTA CACHE 2 #### 
##########################

pergunta="""
Suponha que você é um especialista em testes de carga e estresse, usando jMeter em Java.

Você é capaz de planejar e executar testes de carga e estresse com jMeter em aplicações que expõe APIs REST para avaliar o desempenho, escalabilidade e resiliência destas aplicações a fim de identificar gargalos de performance.

Além de especialista, você corrige provas sobre o tópico. 

Considere a seguinte pergunta e a seguinte resposta:

P: Explique o invalidação de cache em aplicações REST e apresente uma forma de resolve-lo.
R: {}

Qual nota você daria para esta resposta, numa escala de 0 a 10? Pense passo a passo.

Devolva a resposta em um formato JSON, com uma variável 'nota', com a sua nota, e uma outra variável 'explicação', com a explicação para esta nota. 

Sua explicação deve ter ao menos 20 palavras. Escreva a resposta usando UTF-8. Se nenhuma resposta for informada, informe que 'Nenhuma resposta foi informada', e de nota zero.
"""

reposta1 = """
A exemplo do catalogo de e-commerce, toda vez que houver uma atualizacao nos itens do catalogo (mudanca de preco, adicao ou remocao de item, etc) o cache deve ser "invalidado", ou seja, apagado total ou parcialmente; dessa forma quando uma nova requisicao desse catalogo chegar ao servidor nao encontrara uma "chave" que correspondente e automaticamente a requisicao sera "entregue" a aplicacao que ira gerar uma nova resposta atualizada com as informacoes coletadas do banco-de-dados.
"""
resposta2 = """
O problema é ter um cache eterno, em que qualquer mudança de informação não será atualizado em cache. Dado isso, uma forma de solucionar é definir um tempo de expiração para aquela determinada informação em cache, além disso esse tempo depende de como é a frequência da atualização daqueles dados, se for algo que muda muito, talvez o cache não ajude muito.
"""
resposta3 = """
Há duas formas de fazer isso, usando TTL (time to live), onde é definido o tempo que um dado fica armazenado no cache. Então a pessoa programadora verifica o cache, se houver valor, retorna, se não houver, busca na fonte da verdade (normalmente o banco de dados), coloca no cache e retorna.
Outro jeito, é quando a pessoa programadora, tem controle de todo o ciclo de vida do dado, e consegue, colocar no cache o dado toda vez que ele é inserido/alterado e remover do cache toda vez que ele é removido, então o cache pode ser utilizado em consultas, sem a necessidade de fazer um IO mais demorado (memória é mais rápido que disco)
"""
resposta4 = """
A invalidação de cache ocorre quando uma ação é feita que poderia mudar o estado da informação cacheada. No caso de cache por servidor de seu sub-processamento, uma forma de resolver seria a ação de alteração da informação remover o dado do sistema de caching. Outra forma, mais utilizada, porém não tão efetiva de acordo com alguns cenários, é o tempo de existencia do dado no cache (apos X segs o cache seria "removido") ou então a utilização do LFU ou FIFO, onde os dados do caches seriam removidos conforme seu volume de utilização ou ordem de inserção.
"""
resposta5 = """
"""
resposta6 = """
Quando ocorre invalidação do cache, o mesmo é removido do armazenamento e será renovado com uma proxima chamada a API. É possivel agendar a invalidação do cache, dependendo da volatilidade da informacao armazenada.
"""
resposta7 = """
Invalidar um cache é quando sabemos que houve mudança em algum dado, isso pode ser determinado por um tempo pré estabelecido ou invalidando em um determinado ponto da aplicação, exemplo: ao adicionar um novo registro invalide os caches de GET
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
