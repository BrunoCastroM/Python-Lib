from pythonlib.github_api_avatar import github_api


def test_search_avatar():
    url = github_api.search_avatar('BrunoCastroM')
    assert 'https://avatars.githubusercontent.com/u/104720539?v=4' == url
