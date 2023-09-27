from bson import ObjectId
from Database import Database
from Motorista import Motorista


class MotoristaDAO:
    def __init__(self):
        self.db = Database()

    def insert(self, Motorista: Motorista):
        corridas= []
        for corrida in Motorista.corridas:
            corridas.append({"Nota": corrida.nota,
                        "Distancia": corrida.distancia,
                        "Valor": corrida.valor,
                        "NomePassageiro": corrida.nome,
                        "DocumentoPassageiro": corrida.documento})
        try:
            result = self.db.collection.insert_one({"Corridas":corridas})
            print("Corrida inserida com sucesso")
            return result.inserted_id
        except Exception as e:
            print("Ocorreu um erro na inserção ", e)
            return None

    def update(self, motorista_id: str, motorista: Motorista):
        corridas = []
        for corrida in Motorista.corridas:
            corridas.append({"Nota": corrida.nota,
                             "Distancia": corrida.distancia,
                             "Valor": corrida.valor,
                             "NomePassageiro": corrida.nome,
                             "DocumentoPassageiro": corrida.documento})
        try:
            result = self.db.collection.insert_one({"Corridas":corridas})
            return result.modified_count
        except Exception as e:
            print("Ocorreu um erro ao atualizar ", e)
            return None

    def delete(self, motorista_id: str):
        try:
            result = self.db.collection.delete_one({"_id": ObjectId(motorista_id)})
            print("Motorista deletetado com sucesso")
            return result.deleted_count
        except Exception as e:
            print("Ocorreu um erro ao deletar ", e)
            return None

    def read(self, motorista_id: str):
        try:
            result = self.db.collection.find_one({"_id": ObjectId(motorista_id)})
            print("motorista encontrado", result)
            return result
        except Exception as e:
            print("Ocorreu um erro ao ler ", e)
