from Lab import Laboratorio
from CLI import CLI

labs = [Laboratorio("Cidade 1"), Laboratorio("Cidade 2")]

while True:
    i = 1
    for lab in labs:
        print(f"Para o Lab {lab.endereco} selecione {i}")
        i +=1
    command = input("Selecione a Filial: ")
    if command != "1" and command !="2":
        print("Comando não existente, encerrando.")
        break
    break
print(f"Laboratorio escolhido:{labs[int(command)-1].endereco}")
laboratorioCLI = CLI(labs[int(command)-1])
laboratorioCLI.run()
