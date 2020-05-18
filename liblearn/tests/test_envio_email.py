
from liblearn.spam.enviador_email import Enviador, EmailInvalido
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


"""
decoretor importei pytest passando mark e parametrize
nome do parametro é usado como argumento da função
"""


@pytest.mark.parametrize(
    'destinatario',  # parametro
    ['rafaela.piva@yahoo.com.br', 'serluscasas@gmail.com']
    )
def test_rementente(destinatario):  # (argumento da função)
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'serlusmc@yahoo.com.br',
        'teste de envio',
        'primeiro teste de envio de email.'
        )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    [' ', 'rafaela']
    )
def test_rementente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):  # criar sistema de exceções
        enviador.enviar(
            remetente,
            'serlusmc@yahoo.com.br',
            'teste de envio',
            'primeiro teste de envio de email.'
            )
