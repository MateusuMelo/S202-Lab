from database import Database as Data
from writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self):
        self.dataset = Data(database="mercado", collection="produtos")
        self.dataset.resetDatabase()
    def vendasPDia(self):
        data = self.dataset.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"data": "$data_compra"},
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": -1}},
        ])
        return writeAJson(data, "Vendas por dia")

    def maisVendido(self):
        data = self.dataset.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        return writeAJson(data, "Mais vendido")

    def cliente_com_mais_Gasto(self):
        data = self.dataset.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"},
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": -1}},
            {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}},
            {"$limit": 1}
        ])
        return writeAJson(data, "Cliente com mais gasto")

    def produtosVendidos(self):
        data = self.dataset.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}}
        ])
        return writeAJson(data, "Produtos vendidos")
