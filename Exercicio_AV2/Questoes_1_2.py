from query import Database

def crud(query):
    try:
        connection = Database()
        connection.connect()
        result = connection.execute_query(query)
    except Exception as e:
        print(f"Erro: {str(e)}")
    finally:
        connection.close()
    return result



#Questão 1 a
print("Questão 1 a:")
queryq1 = "Match(t:Teacher{name:'Renzo'}) return t.ano_nasc as Ano_nasc, t.cpf as CPF"
q1_result = crud(queryq1)
for line in q1_result:
    for key, value in line.items():
        print(f'{key} : {value}')


#Questão 1 b
print("Questão 1 b:")
queryq1b = "Match(t:Teacher) where t.name STARTS WITH 'M' RETURN t.name as Nome, t.cpf as CPF"
q1b_result = crud(queryq1b)
for line in q1b_result:
    for key, value in line.items():
        print(f'{key} : {value}')

    print('\n')
        
#Questão 1 c
print("Questão 1 c:")
queryq1c = "MATCH (n:City) RETURN n.name as Cidade"
q1c_result = crud(queryq1c)
for line in q1c_result:
    for key, value in line.items():
        print(f'{key} : {value}')

    print('\n')

#Questão 1 d
print("Questão 1 d:")
queryq1d = "MATCH (n:School) WHERE n.number >=150 AND n.number<= 550 return n.address as endereco, n.number as numero"
q1d_result = crud(queryq1d)
for line in q1d_result:
    for key, value in line.items():
        print(f'{key} : {value}')

    print('\n')    

#Questao 2 a
print("Questão 2 a:")
queryq2a = "MATCH (n:Teacher) WITH min(n.ano_nasc) as maisVelho, max(n.ano_nasc) as MaisNovo return maisVelho, MaisNovo"
q2a_result = crud(queryq2a)
for line in q2a_result:
    for key, value in line.items():
        print(f'{key} : {value}')

#Questao 2 b
print("Questão 2 b:")
queryq2b = "MATCH (n:City) WITH avg(n.population) as Media return Media"
q2b_result = crud(queryq2b)
for line in q2b_result:
    for key, value in line.items():
        print(f'{key} : {value}')

#Questao 2 c
print("Questão 2 c:")
queryq2c = "MATCH (c:City) WHERE c.cep = '37540-000' RETURN replace(c.name, 'a', 'A') AS Cidade"
q2c_result = crud(queryq2c)
for line in q2c_result:
    for key, value in line.items():
        print(f'{key} : {value}')

#Questao 2 d
print("Questão 2 d:")
queryq2d = "MATCH (t:Teacher) RETURN substring(t.name, 2, 1) AS Caracter"
q2d_result = crud(queryq2d)
for line in q2d_result:
    for key, value in line.items():
        print(f'{key} : {value}')
