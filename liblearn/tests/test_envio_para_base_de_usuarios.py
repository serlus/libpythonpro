from liblearn.spam.models import Usuario
import pytest
from liblearn.spam.enviador_email import Enviador
from liblearn.spam.main import EnviadorDeSpam

@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Sergio', email='serluscasas@gmail.com'),
            Usuario(nome='Luciano', email='luciano@gmail.com')
        ]
        [
            Usuario(nome='Sergio', email='serluscasas@gmail.com')
        ]
    ]
)
def test_qd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'serlusmc@yahoo.com.br',
        'Curso python Pro',
        'Confirma os módulos fantásticos'
    )
    assert len(usuarios) == enviador.gtd_email_enviados