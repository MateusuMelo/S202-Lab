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
    def __init__(self, teacher_crud):
        super().__init__()
        self.teacher_crud = teacher_crud
        self.add_command("create", self.create)
        self.add_command("read", self.read)
        self.add_command("update", self.update)
        self.add_command("delete", self.delete)

    def create(self):
        name = str(input("Entre com o nome: "))
        ano_nasc = int(input("Entre com a data de nascimento: "))
        cpf = str(input("Entre com o cpf: "))
        self.teacher_crud.create(name,ano_nasc,cpf)

    def read(self):
        name = str(input("Entre com o nome: "))
        result = self.teacher_crud.read(name)
        for line in result:
            for key, value in line['t'].items():
                print(f'{key} : {value}')

    def update(self):
        name = str(input("Entre com o nome: "))
        newCpf = str(input("Entre com o novo cpf: "))
        self.teacher_crud.create(name,newCpf)

    def delete(self):
        name = str(input("Entre com o nome: "))
        self.teacher_crud.dedlete(name)
        
    def run(self):
        print("Welcome to the Teacher CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()