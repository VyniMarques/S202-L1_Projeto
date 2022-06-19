from db.database import Graph
from classes.jogo import Jogo


class Locadora:
    jogo = Jogo()

    def __init__(self):
        self.db = Graph(uri='bolt://3.84.44.165:7687',
                        user='neo4j', password='apportionment-regions-subprograms')

    def create_locadora(self, nome, numFuncionarios, faturamento):
        return self.db.execute_query(
            'CREATE (n:Locadora {nome:$nome, numFuncionarios:$numFunionarios, faturamento:$faturamento}) return n',
            {'nome': nome, 'numFunionarios': numFuncionarios, 'faturamento': faturamento})

    def read_funcionario(self):
        return self.db.execute_query('MATCH (n:Funcionario) RETURN n')

    def read_clientes(self):
        return self.db.execute_query('MATCH (n:Cliente) RETURN n')

    def read_locadora(self):
        aux = self.db.execute_query('MATCH (n:Locadora) RETURN n')
        return len(aux) != 0
