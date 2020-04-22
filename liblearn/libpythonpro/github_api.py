import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no Github

    :para usuarios: str com o nome de usuário no github
    :return: str com o link do avatar json serve como 
     dicionario e dentro da chave digo o q quero buscar
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']

if __name__ == '__main__':  
    print(buscar_avatar('serlus'))