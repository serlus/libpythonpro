from unittest.mock import Mock
from liblearn import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login':	'serlus', 'id':	63012359,
        'avatar_url':	'https://avatars0.githubusercontent.com/u/63012359?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('serlus')
    assert 'https://avatars0.githubusercontent.com/u/63012359?v=4' == url

def test__buscar_repositorios():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login':	'serlus', 'id':	63012359,
        'repos_url':	'https://api.github.com/users/serlus/repos',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url_2 = github_api.buscar_repositorios('serlus')
    assert 'https://api.github.com/users/serlus/repos' == url_2
