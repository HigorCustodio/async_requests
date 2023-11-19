Requests assíncronos com HTTPX:

Objetivo:
    Identificar, exemplificar e realizar a migração de uma base de conhecimento realizada através de requests sincronos, para
    assíncronos.

    Neste exemplo será contruido uma base de dados sobre pokemons, com objetivo de mapear as evoluções 
    dos pokemons apartir de um nome passado para a requisição.
    
    API Utilizada: pokeAPI;

HTTPX:

    Biblioteca para realizar requests web;
    •   Desenhada para requisições async;
    •   Suporta HTTP 1.1 e 2.0;
    •   Suporta:
        -   asyncio;
        -   Trio;
        -   Anyio;
    
    Instalação: pip install httpx


Utilização:
    Métodos: Get, Patch, Post e Delete;
    
    Argumentos gerais:
        params = {}"
        URL = str
        headers = {}
        json = {}
        cookies = {}
        auth = {}


    Respostas:
        ex:
        >>> Entrada:
            response = httpx.get('url')

        >>> Saída:
            response
            response.text
            response.json()
            response.content
            response.status_code
            response.headers 
            response.cookies  (informações armazenadas da sessão pelo Client)
            response.history  (histórico de redirecionamento(requests intermediários - Só funciona no método get))

    Timeout padrão: 0.5 segundos;
