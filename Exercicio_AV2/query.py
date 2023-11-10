from neo4j import GraphDatabase
# Classe para lidar com a conexão e transações do Neo4j
class Database:
    def __init__(self):
        pass
    
    def connect(self):
        self._driver = GraphDatabase.driver('neo4j+s://f08621b4.databases.neo4j.io', auth=('neo4j', 'UtRsFSYanL1-Mvj1uZ4War-uiW-oicu-y8LizZoLbpA'))

    def close(self):
        self._driver.close()

    def execute_query(self, query, **kwargs):
        with self._driver.session() as session:
            result = session.execute_write(self._execute, query, **kwargs)
            return result

    @staticmethod
    def _execute(tx, query, **kwargs):
        result = tx.run(query, **kwargs)
        return result.data()
