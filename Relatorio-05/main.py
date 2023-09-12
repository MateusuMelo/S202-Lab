import pprint

from crud import LivroModel
from pymongo import MongoClient
from cli import livroCLI

client = MongoClient("mongodb://localhost:27017")
db = client['Relatorio_05']
biblioteca = db.Biblioteca

livroModel = LivroModel(database=biblioteca)

livrocli = livroCLI(livroModel)
livrocli.run()