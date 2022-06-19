from db.database import Graph
from classes.jogo import Jogo


class Pessoa:

    def __init__(self):
        self.db = Graph(uri='bolt://3.84.44.165:7687',
                        user='neo4j', password='apportionment-regions-subprograms')

    def create_pessoa(self, nome, numero, endereco, email):
        return self.db.execute_query(
            'CREATE (n:Pessoa {nome:$nome, numero:$numero, endereco:$endereco, email:$email}) return n',
            {'nome': nome, 'numero': numero, 'endereco': endereco, 'email': email})

    def is_alugado(self, nome):
        jogo = Jogo()
        jogo.is_alugado(nome)
