from numpy import double
from bson.objectid import ObjectId

class LivroModel:
    def __init__(self, database):
        self.db = database

    def Inserir_Livro(self, titulo:str, autor:str, ano: int, preco: double):
        try:
            res = self.db.insert_one({"titulo": titulo, "autor": autor, "ano":ano,"preco":preco})
            print(f"book created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating book: {e}")
            return None

    def livro_pelo_id(self, id: str):
        try:
            res = self.db.find_one({"_id": ObjectId(id)})
            print(f"Book found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading book: {e}")
            return None

    def update_livro(self, id: str,titulo:str, autor:str, ano: int, preco: double):
        try:
            res = self.db.update_one({"_id": ObjectId(id)}, {"$set": {"titulo": titulo, "autor": autor, "ano":ano,"preco":preco}})
            print(f"book updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating book: {e}")
            return None

    def delete_livro(self, id: str):
        try:
            res = self.db.delete_one({"_id": ObjectId(id)})
            print(f"book deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting book: {e}")
            return None