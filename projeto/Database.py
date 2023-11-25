import pymongo

class Database:
    def __init__(self):
        pass

    def connect(self):
        try:
            self.ClusterConnectrion = pymongo.MongoClient("mongodb://localhost:27017")
            self.db = self.ClusterConnectrion['projeto']
            self.collection = self.db['Lab']
            print(type(self.db))
            print("conectado ao banco com sucesso")
        except Exception as e:
            print("Um erro ocorreu ", e)

    def close(self):
        self.ClusterConnectrion.close()

    def insert(self,document):
        try:
            self.connect()
            result = self.collection.insert_one(document)
            return result
        except Exception as e:
            print(e)
        finally:
            self.close()

    def find(self, query):
        try:
            self.connect()
            result = self.collection.find_one(query)
            return result
        except Exception as e:
            print(e)
        finally:
            self.close()

    def update(self, query, update):
        try:
            self.connect()
            result = self.collection.update_one(query, {'$set': update})
            return result
        except Exception as e:
            print(e)
        finally:
            self.close()

    def delete(self, query):
        try:
            self.connect()
            result = self.collection.delete_one(query)
            return result
        except Exception as e:
            print(e)
        finally:
            self.close()
        