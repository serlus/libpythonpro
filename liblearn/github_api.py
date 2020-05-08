import requests
"""
    Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \**kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response

    """


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no Github

    :param usuario: str com o nome de usuário no github
    :return: str com o link do avatar
    json serve como dicionario e dentro da chave digo o q quero buscar
    """

    url = f'https://api.github.com/users/{usuario}' # url da pagina onde tem a info
    resp = requests.get(url) 
    return resp.json()['avatar_url']


def repositorios(usuario):
    """
    Busca reposiotorios dentro do GitHub

    :param usuario: str nome de usuario no github
    :return: str com o link dos repositorios
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['repos_url']


if __name__ == '__main__':
    print(buscar_avatar('serlus'))
    print(repositorios('serlus'))
    