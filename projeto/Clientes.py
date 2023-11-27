from Exame import Exame
from Database import Database

class Cliente:
    def __init__(self, nome:str, cpf:str):
        self.nome = nome
        self.cpf = cpf
        self.database = Database()
        try:
            self.exames = self.database.find({"Nome": f"{nome}"})['Exames']
        except Exception as e:
            print(e)
            self.exames = []
        
    def pedido(self, responsavel:str, tipo:str):
        gen_exame = Exame(responsavel,tipo)
        set_exame = gen_exame.gerarPedidoExame()

        update_data = {"$push": {"Exames": set_exame}}
        query = {"Nome": f"{self.nome}"}
        self.database.update(query, update_data)
        self.exames.append(gen_exame)
        return None
    def concluirExame(self,dataExame:str):
        query = {"Nome": f"{self.nome}", "Exames.DataPedido": f"{dataExame}"}
        self.database.update(query, {"$set": {"Exames.$.Status": "concluido"}})
        for exame in self.exames:
            if(exame['DataPedido'] == dataExame):
                set_exame = Exame(exame['Responsavel'], exame['Tipo']).concluirPedidoExame(exame['DataPedido'])
                update_data = {
                    "$set": {
                        "Exames.$": set_exame
                    }
                }
                self.database.update(query, update_data)
        return None