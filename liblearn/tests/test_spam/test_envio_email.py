from liblearn.spam.enviador_email import Enviador


class Enviador:
    pass

def test_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None

def test_rementente():
    enviador=Enviador()
    resultado = enviador.enviar(
        'serluscasas@gmail.com',
        'serlusmc@yahoo.com.br',
        'teste de envio',
        'primeiro teste de envio de email.'
        )
    assert 'serluscasas@gmail.com' in resultado