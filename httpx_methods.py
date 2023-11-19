import httpx


def get():
    #Simples:
    response = httpx.get('https://httpbin.org/get')

    #Resposta:
    json = response.json()
    # print(response)
    # print(response.json())
    return json


def get_follow_redirect():
    #Follow Redirect:
    #   Usado para retornar os redirecionamentos de requests (requests intermediários);
    response = httpx.get(
        url='https://httpbin.org/redirect/10',
        follow_redirects=True
    )
    history = response.history
    # print(response.history)

    #   É possível acessar cada request do history armazenado:
    history[0]
    # print(response.history[0].status_code)
    # print(response.history[0].content)
    
    return history


def get_change_timeout(timeout:float):
    #TimeOut:
    #   Por padrão o tempo de requisição é 0.5;
    #   Caso não queira aplicar um timeout, é possível passar o valor None para o parâmetro.
    response = httpx.get(
        url='https://httpbin.org/get',
        timeout=timeout
    )
    
    
    return response

def post():
    response = httpx.post('https://httpbin.org/post')
    # print(response)
    # print(response.text)
    # print(response.json())
    # print(response.content)
    return response
    
def patch():
    response = httpx.patch('https://httpbin.org/patch')
    # print(response)
    # print(response.text)
    # print(response.json())
    # print(response.content)
    # print(response.status_code)
    return response

def delete():
    response = httpx.delete('https://httpbin.org/delete')
    # print(response)
    # print(response.text)
    # print(response.content)
    return response