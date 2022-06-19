from db.database import Graph
from classes.pessoa import Pessoa
from classes.jogo import Jogo


class Funcionario(Pessoa):

    def __init__(self):
        self.db = Graph(uri='bolt://3.84.44.165:7687',
                        user='neo4j', password='apportionment-regions-subprograms')

    def create_aux(self, email, dataComecou, cargo):
        self.db.execute_query(
            'MATCH (n:Pessoa {email:$email}) SET n.dataComecou = $dataComecou, n.cargo = $cargo, n:Funcionario RETURN '
            'n;',
            {'email': email, 'dataComecou': dataComecou, 'cargo': cargo})
        self.db.execute_query('MATCH (l:Locadora),(p:Pessoa{email:$email}) Create (p)-[:TRABALHA_EM]->(l)',
                              {'email': email})
        self.db.execute_query('MATCH (l:Locadora) SET l.numFuncionarios = l.numFuncionarios  + 1 ')

    def create_pessoa(self, nome, numero, endereco, email, dataComecou, cargo):
        super().create_pessoa(nome, numero, endereco, email)
        self.create_aux(email, dataComecou, cargo)

    def adiciona_jogo(self, jogo):
        jogo1 = Jogo()
        jogo1.create(jogo)

    def deleta_jogo(self, nome):
        jogo = Jogo()
        jogo.delete(nome)

    def deleta_cliente(self, nome):
        return self.db.execute_query('MATCH (c:Cliente{nome:$nome}) DETACH DELETE c',
                                     {'nome': nome})

    def deleta_funcionario(self, nome):
        self.db.execute_query('MATCH (f:Funcionario{nome:$nome}) DETACH DELETE f',
                              {'nome': nome})
        self.db.execute_query('MATCH (l:Locadora) SET l.numFuncionarios = l.numFuncionarios  - 1 ')

    def emailCliente(self, nome, email):
        return self.db.execute_query(
            'MATCH (c:Cliente{nome:$nome}) set c.email = $email',
            {'nome': nome, 'email': email})
