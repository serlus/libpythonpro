from liblearn.spam.models import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Sergio', email='serluscasas@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Sergio', email='serluscasas@gmail.com'), Usuario(nome='Luciano', email='luciano@gmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
