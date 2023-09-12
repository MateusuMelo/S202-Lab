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


class livroCLI(SimpleCLI):
    def __init__(self, livro_model):
        super().__init__()
        self.livro_model = livro_model
        self.add_command("create", self.create_livro)
        self.add_command("read", self.read_livro)
        self.add_command("update", self.update_livro)
        self.add_command("delete", self.delete_livro)

    def create_livro(self):
        title = input("Enter the title: ")
        author = str(input("Enter the author: "))
        age = int(input("Enter the age: "))
        price = float(input("Enter the price: "))
        self.livro_model.Inserir_Livro(title, author, age, price)

    def read_livro(self):
        id = input("Enter the id: ")
        livro = self.livro_model.livro_pelo_id(id)
        if livro:
            print(f"Title: {livro['titulo']}")
            print(f"Author: {livro['autor']}")
            print(f"Age: {livro['ano']}")
            print(f"Price: {livro['preco']}")

    def update_livro(self):
        id = input("Enter the id: ")
        title = input("Enter the new title: ")
        author = input("Enter the new author: ")
        age = int(input("Enter the new age: "))
        price = float(input("Enter the new price: "))
        self.livro_model.update_livro(id,title, author, age, price)

    def delete_livro(self):
        id = input("Enter the id: ")
        self.livro_model.delete_livro(id)
        
    def run(self):
        print("Welcome to the livro CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        
