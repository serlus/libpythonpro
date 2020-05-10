from liblearn.spam.enviador_email import Enviador
from liblearn.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'serlusmc@yahoo.com.br',
        'Curso python Pro',
        'Confirma os módulos fantásticos'
    )
