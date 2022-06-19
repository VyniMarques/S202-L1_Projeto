from db.database import Graph
from classes.pessoa import Pessoa
from classes.jogo import Jogo


class Cliente(Pessoa):

    def __init__(self):
        self.db = Graph(uri='bolt://3.84.44.165:7687',
                        user='neo4j', password='apportionment-regions-subprograms')

    def create_aux(self, email, numJogoAlugado, dataCriacao):
        self.db.execute_query(
            'MATCH (n:Pessoa {email:$email}) SET n.numJogoAlugado = $numJogoAlugado, n.dataCriacao = $dataCriacao, '
            'n:Cliente RETURN n',
            {'email': email, 'numJogoAlugado': numJogoAlugado, 'dataCriacao': dataCriacao})
        self.db.execute_query('MATCH (l:Locadora),(p:Pessoa{email:$email}) Create (p)-[:ALUGA_EM]->(l)',
                              {'email': email})

    def create_pessoa(self, nome, numero, endereco, email, numJogoAlugado, dataCriacao):
        super().create_pessoa(nome, numero, endereco, email)
        self.create_aux(email, numJogoAlugado, dataCriacao)

    def alugar(self, email, nome, data):
        jogo = Jogo()
        jogo.alugar_jogo(email, nome, data)
        self.db.execute_query('MATCH (c:Cliente) SET c.numJogoAlugado = c.numJogoAlugado  + 1 ')

    def devolver(self, email, nome):
        jogo = Jogo()
        jogo.devolver_jogo(email, nome)
        self.db.execute_query('MATCH (c:Cliente) SET c.numJogoAlugado = c.numJogoAlugado  - 1 ')