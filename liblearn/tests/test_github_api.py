import pytest
from unittest.mock import Mock
from liblearn import github_api



@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/63012359?v=4'
    resp_mock.json.return_value = {
        'login':	'serlus', 'id':	63012359,
        'avatar_url': url,
    }
    get_original = github_api.requests.get  # setup
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original  # Tear Down

def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('serlus')
    assert avatar_url == url

def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('serluss')
    assert 'https://avatars0.githubusercontent.com/u/63012359?v=4' == url
    
# def test_buscar_repositorios():
#     resp_mock = Mock()
#     resp_mock.json.return_value = {
#         'login':	'serlus', 'id':	63012359,
#         'repos_url':	'https://api.github.com/users/serlus/repos',
#     }
#     github_api.requests.get = Mock(return_value=resp_mock)
#     url_2 = github_api.buscar_repositorios('serlus')
#     assert 'https://api.github.com/users/serlus/repos' == url_2
