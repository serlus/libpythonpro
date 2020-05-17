import pytest
from unittest.mock import Mock
from liblearn import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars0.githubusercontent.com/u/63012359?v=4'
    resp_mock.json.return_value = {
        'login':	'serlus', 'id':	63012359,
        'avatar_url': url,
         avatar_integracao 
    }
    get_mock = mocker.patch('liblearn.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('serlus')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('serlus')
    assert 'https://avatars0.githubusercontent.com/u/63012359?v=4' == url


@pytest.fixture
def repos_url(mocker):
    resp_mock = Mock()
    url_2 = 'https://api.github.com/users/serlus/repos',
    resp_mock.json.return_value = {
        'login':	'serlus', 'id':	63012359,
        'repos_url':	url_2
    }
    get_mock = mocker.patch('liblearn.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url_2


def test_buscar_repositorios(repos_url):
    url_2 = github_api.buscar_repositorios('serlus')
    assert repos_url == url_2


def test_buscar_repositorios_integracao():
    url_2 = github_api.buscar_repositorios('serlus')
    assert 'https://api.github.com/users/serlus/repos' == url_2
