from Clientes import Cliente
from Database import Database
class Laboratorio:
    def __init__(self, entereco:str):
        self.endereco = entereco
        self.clientes:Cliente = []
        self.data = Database()

    def cadastro(self,nome:str, cpf:str):
        cliente ={
                    "Nome": f"{nome}",
                    "Cpf": f"{cpf}",
                    "Exame": {}
                }
        self.data.insert(cliente)

    def buscaCliente(self, nome:str):
        query = {"Nome":f"{nome}"}
        return self.data.find(query)

    def removeCliente(self, nome:str):
        query = {"Nome":f"{nome}"}
        return self.data.delete(query)
        