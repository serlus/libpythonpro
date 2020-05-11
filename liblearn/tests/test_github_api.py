from liblearn import github_api


def test_buscar_avatar():
    # resp_mock = Mock()
    # resp_mock.json
    url = github_api.buscar_avatar('serlus')
    assert 'https://avatars0.githubusercontent.com/u/63012359?v=4' == url