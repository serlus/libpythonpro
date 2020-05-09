
from spam.enviador_email import Enviador
import pytest


class Enviador:


    def test_criar_enviador_de_email():
        enviador=Enviador()
        assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['serlusmc@yahoo.com.br', 'rafaela.piva@yahoo.com.br']
    )

def test_rementente():
    enviador=Enviador()
    resultado = enviador.enviar(
        rementente,
        'serlusmc@yahoo.com.br',
        'teste de envio',
        'primeiro teste de envio de email.'
        )
    assert destinatario in resultado


class EmailInvalido:


    @pytest.mark.parametrize(
        'remetente',
        [' ', 'rafaela']
        )

    def test_rementente_invalido(remetente):
        enviador=Enviador()
        with pytest.raises(EmailInvalido):
            enviador.enviar(
                remetente,
                'serlusmc@yahoo.com.br',
                'teste de envio',
                'primeiro teste de envio de email.'
                )
        assert remetente in resultado
