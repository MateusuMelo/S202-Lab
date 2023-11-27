from Clientes import Cliente
from Database import Database
class Laboratorio:
    def __init__(self, entereco:str):
        self.endereco = entereco
        self.data = Database()

    def cadastro(self,cliente:Cliente):
        cliente ={
                    "Nome": f"{cliente.nome}",
                    "Cpf": f"{cliente.cpf}",
                    "Exames": []
                }
        self.data.insert(cliente)

    def buscaCliente(self, nome:str):
        query = {"Nome":f"{nome}"}
        result = self.data.find(query)
        print(result)
        return result

    def removeCliente(self, nome:str):
        query = {"Nome":f"{nome}"}
        result = self.data.delete(query)
        print(result)
        return result


