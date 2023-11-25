from datetime import datetime
from Database import Database
class Exame:
    def __init__(self, responsavel:str ,tipo:str):
        self.responsavel = responsavel
        self.tipo = tipo
        self.data = datetime.now()

    def gerarPedidoExame(self, nome: str):
        query = {"Nome":f"{nome}"}
        set = {"Exame.Status":"pedido",
               "Exame.DataPedido":f"{self.data}",
               "Exame.Responsavel": f"{self.responsavel}",
               "Exame.Tipo":f"{self.tipo}"}
        self.data.update(query,set)

    def ConcluirPedidoExame(self, nome: str):
        query = {"Nome":f"{nome}"}
        set = {"Exame.Status":"Concluido",
               "Exame.DataConcluido":f"{self.data}",
               "Exame.Resultado":"Exame.pdf"}
        self.data.update(query,set)
    


        