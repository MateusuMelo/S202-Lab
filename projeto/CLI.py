from Lab import Laboratorio
from Clientes import Cliente
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


class CLI(SimpleCLI):
    def __init__(self, Lab:Laboratorio):
        super().__init__()
        self.Lab: Laboratorio = Lab
        self.add_command("Cadastro", self.cadastro)
        self.add_command("Buscar", self.buscar)
        self.add_command("remover", self.remover)

    def cadastro(self):
        print("Menu de cadastro ")
        nome = str(input("Entre com o nome: "))
        cpf = input("Entre com o Cpf: ")
        self.Lab.cadastro(Cliente(nome,cpf))

    def buscar(self):
        print("--------Menu de busca de Clientes")
        nome = str(input("Entre com o nome completo: "))
        result = self.Lab.buscaCliente(nome)
        if result != None:
            print("Cliente encontrado : ")
            print("Nome: ",result.nome)
            print("Cpf: ", result.cpf)
            print("Exames: ")
            for exame in result.exames:
                for key, value in exame.items():
                    print(f"{key} : {value}")
            print("======================")
            while True:
                print("-----Opcoes do Cliente: ")
                print("--- MENU CLIENTE --- Para gerar um pedido exame digite: Pedido")
                print("--- MENU CLIENTE --- Para Concluir um exame: Concluir")
                opcao = input("--- MENU CLIENTE --- Insira um comando: ")
                if opcao == "Pedido":
                    responsavel = input("Insira o Nome do responsavel pelo exame: ")
                    tipo = input("Insira o tipo do exame: ")
                    result.pedido(responsavel,tipo)
                    break
                elif opcao == "Concluir":
                    data = input("Insira a data do pedido do exame: ")
                    result.concluirExame(data)
                    break
                else:
                    print("opcao invalida")
                    break
    def remover(self):
        nome = str(input("Entre com o nome do cliente a ser removido: "))
        self.Lab.removeCliente(nome)

    def run(self):
        print("Bem vindo ao Laboratorio CLI!")
        print("Comandos Disponiveis: Cadastro, Buscar, Remover, quit")
        super().run()