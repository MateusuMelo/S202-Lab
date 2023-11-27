from datetime import datetime
class Exame:
    def __init__(self, responsavel:str ,tipo:str):
        self.responsavel = responsavel
        self.tipo = tipo
        self.data = str(datetime.today().strftime('%d/%m/%Y'))

    def gerarPedidoExame(self):

        args = {"Status":"pedido",
               "DataPedido":f"{self.data}",
               "Responsavel": f"{self.responsavel}",
               "Tipo":f"{self.tipo}"}
        return args


    def concluirPedidoExame(self,dataPedido):

        args = {"Status":"Concluido",
                "DataPedido": f"{dataPedido}",
                "Tipo": f"{self.tipo}",
                "DataConcluido":f"{str(datetime.today().strftime('%d/%m/%Y'))}",
                "Resultado":"Exame.pdf"}
        return args
