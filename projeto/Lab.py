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
        try:
            self.data.insert(cliente)
            print("Cadastrado com Sucesso")
        except Exception as e:
            print("Ocorreu um erro ao cadastrar, erro:", e)


    def buscaCliente(self, nome:str):
        query = {"Nome":f"{nome}"}
        try:
            result = self.data.find(query)

            client = Cliente(result['Nome'],result['Cpf'])
            return client
        except Exception as e:
            print("Ocorreu um erro ao buscar, erro:", e)
            return None


    def removeCliente(self, nome:str):
        query = {"Nome":f"{nome}"}
        try:
            result = self.data.delete(query)
            print(result)
            return result
        except Exception as e:
            print("Ocorreu um erro ao Deletar, erro:", e)
