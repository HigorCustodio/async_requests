from httpx import Client

'''
    Cria uma sessão onde é possível manter informações armazenadas por um determinado "periódo";
    
    Classe Client() semelhante a classe sessions() da biblioteca do requests;
    
    Utilizando o with é possível executar diversas tarefas dentro do contexto do cliente;
    
    Client():
        Parâmetros:
            •   É possível passar parâmetros para a classe Client(), desta forma, utilizando o with em conjunto com o Client(), os parâmetros recebidos irão perssistir até o fim do bloco de código, o que gera em menor repetição de linhas, onde, por exemplo em toda requisição seria passada a mesma "base_url"
            utilizando o with e o Client() é possível passa-la somente na instância da classe.
            
            - base_url;
            - timeout;
            - cookies;
            - headers;
'''


with Client(base_url='https://httpbin.org/') as client:
    response = client.get(
        url='get',
    )

print(response)