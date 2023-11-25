from Exame import Exame
from Database import Database

class Cliente:
    def __init__(self, nome:str, cpf:str):
        self.Exames: Exame = []
        self.nome = nome
        self.cpf = cpf
        self.data = Database()
        
    def pedido(self, responsavel:str, tipo:str):
        Exame.append(Exame(responsavel,tipo).gerarPedidoExame(self.nome))
    def concluirExame(self):
        pass