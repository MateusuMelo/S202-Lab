from query import Database

class TeacherCRUD:
    def __init__(self):
        self.connection = Database()
    
    def create(self, name, ano_nasc, cpf):
        query = f"CREATE(:Teacher{{name:'{name}',ano_nasc:{ano_nasc},cpf:'{cpf}'}});"
        try:
            self.connection.connect()
            result = self.connection.execute_query(query)
            print("Criado com sucesso")
        except Exception as e:
            print(str(e))
        finally:
            self.connection.close()

        return result

    def read(self,name):
        query = f"MATCH (t:Teacher{{name:'{name}'}}) RETURN t"
        try:
            self.connection.connect()
            result = self.connection.execute_query(query)
        except Exception as e:
            print(e)
        finally:
            self.connection.close()

        return result

    def delete(self, name):
        query = f"MATCH (t:Teacher{{name:'{name}'}}) DELETE t"
        try:
            self.connection.connect()
            result = self.connection.execute_query(query)
            print("Deletado com Sucesso")
        except Exception as e:
            print(e)
        finally:
            self.connection.close()

        return result
    
    def update(self, name, newCpf):
        query = f"MATCH (t:Teacher{{name:'{name}'}}) SET t.cpf = '{newCpf}' return t"
        try:
            self.connection.connect()
            result = self.connection.execute_query(query)
            print("Atualizado com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.connection.close()

        return result

#Questao 3a
crud = TeacherCRUD()

#Questao 3b
crud.create('Chris Lima', 1956,'189.052.396-66')

#Questao 3c
read = crud.read('Chris Lima')
for line in read:
    for key, value in line['t'].items():
        print(f'{key} : {value}')

#Questao 3d
crud.update('Chris Lima',"162.052.777-77")

