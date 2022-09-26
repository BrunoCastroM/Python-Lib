import requests


def search_avatar(user):
    """
    Search a user avatar on github

    user: str with username on github
    return: str with avatar link

    """
    url = f'https://api.github.com/users/{user}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']


if __name__ == '__main__':
    print(search_avatar('BrunoCastroM'))
