from Passageiro import Passageiro


class Corrida(Passageiro):
    def __init__(self, nota: int, distancia: float, valor: float, nome: str, documento: str):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor

        Passageiro.__init__(self, nome, documento)
