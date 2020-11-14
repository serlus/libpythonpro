from time import sleep


class Sessao():
    contador = 0
    usuarios = []

    def salvar(self, usuario):
        self.newmethod179() += 1
        usuario.id = self.newmethod179()
        self.usuarios.append(usuario)

    def newmethod179(self):
        return Sessao.contador

    def listar(self):
        return self.usuarios

    def roll_back(self):  # para a teste
        self.usuarios.clear()

    def fechar(self):
        pass


class Conexao:

    def __init__(self):
        sleep(1)

    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass
