from MotoristaDAO import MotoristaDAO
from Motorista import Motorista
from Corrida import Corrida
from Passageiro import Passageiro


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self):
        super().__init__()
        self.MotoristaDAO = MotoristaDAO()
        self.add_command("Inserir", self.insert)
        self.add_command("Atualizar", self.update)
        self.add_command("Deletar", self.delete)
        self.add_command("Ler", self.read)

    def insert(self):
        passageiro_nome = input("Nome do passageiro")
        passageiro_documento = input("Documento do passageiro")
        passageiro = Passageiro(passageiro_nome, passageiro_documento)

        num_corridas = input("Numero de corridas")
        corridas = []
        for i in range(int(num_corridas)):
            corrida_nota = input("Nota da corrida")
            corrida_distancia = input("Distancia da corrida")
            corrida_valor = input("Valor da corrida")
            corridas.append(
                Corrida(corrida_nota, corrida_distancia, corrida_valor, passageiro.nome, passageiro.documento))

        motorista_nota = input("Nota do motorista")
        motorista = Motorista(motorista_nota)
        motorista.corridas = corridas
        self.MotoristaDAO.insert(motorista)

    def update(self):
        motorista_id = input("Insira o id do motorista")

        passageiro_nome = input("Nome do passageiro")
        passageiro_documento = input("Documento do passageiro")
        passageiro = Passageiro(passageiro_nome, passageiro_documento)

        num_corridas = input("Numero de corridas")
        corridas = []
        for i in range(num_corridas):
            corrida_nota = input("Nota da corrida")
            corrida_distancia = input("Distancia da corrida")
            corrida_valor = input("Valor da corrida")
            corridas.append(
                Corrida(corrida_nota, corrida_distancia, corrida_valor, passageiro.nome, passageiro.documento))

        motorista = Motorista(input("Nota do motorista"))
        motorista.corridas = corridas

        self.MotoristaDAO.update(motorista_id, motorista)
    
    def delete(self):
        motorista_id = input("Insira o id do motorista")
        self.MotoristaDAO.delete(motorista_id)
        
    def read(self):
        motorista_id = input("Insira o id do motorista")
        self.MotoristaDAO.read(motorista_id)
        
    def run(self):
        super().run()