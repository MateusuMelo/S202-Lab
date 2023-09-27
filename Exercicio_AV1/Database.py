import pymongo


class Database:
    def __init__(self):
        self.connect()

    def connect(self):
        try:
            self.ClusterConnectrion = pymongo.MongoClient("mongodb+srv://root:root@cluster0.dib4czr.mongodb.net/")
            self.db = self.ClusterConnectrion['Exercicio_Av1']
            self.collection = self.db['Motoristas']
            print(type(self.db))
            print("conectado ao banco com sucesso")
        except Exception as e:
            print("Um erro ocorreu ", e)
