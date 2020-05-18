from liblearn.spam.models import Usuario
import pytest
from unittest.mock import Mock
from liblearn.spam.enviador_email import Enviador
from liblearn.spam.main import EnviadorDeSpam


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Sergio', email='serluscasas@gmail.com'),
            Usuario(nome='Luciano', email='luciano@gmail.com')
        ],
        [
            Usuario(nome='Sergio', email='serluscasas@gmail.com')
        ]
    ]
)
def test_qd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'serlusmc@yahoo.com.br',
        'Curso python Pro',
        'Confirma os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Sergio', email='serluscasas@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'serlusmc@yahoo.com.br',
        'Curso python Pro',
        'Confirma os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'serlusmc@yahoo.com.br',
        'serluscasas@gmail.com',
        'Curso python Pro',
        'Confirma os módulos fantásticos'
    )
