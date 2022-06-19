from db.database import Graph


class Jogo(object):
    def __init__(self):
        self.db = Graph(uri='bolt://3.84.44.165:7687',
                        user='neo4j', password='apportionment-regions-subprograms')

    def create(self, jogo):
        self.db.execute_query('CREATE (j:Jogo {nome:$nome, dataLancamento:$dataLancamento,'
                              'desenvolvedora:$desenvolvedora, genero:$genero}) return j',
                              {'nome': jogo['nome'], 'dataLancamento': jogo['datalancamento'],
                               'desenvolvedora': jogo['desenvolvedora'],
                               'genero': jogo['genero']})
        self.db.execute_query('MATCH (l:Locadora),(j:Jogo{nome:$nome}) Create (j)<-[:POSSUI]-(l)',
                              {'nome': jogo['nome']})

    def read_by_name(self, nome):
        return self.db.execute_query('MATCH (j:Jogo {nome:$nome}) RETURN j',
                                     {'nome': nome})

    def read_all_nodes(self):
        return self.db.execute_query('MATCH (j:Jogo) RETURN j.nome')

    def delete(self, nome):
        return self.db.execute_query('MATCH (j:Jogo{nome:$nome}) DETACH DELETE j',
                                     {'nome': nome})

    def alugar_jogo(self, email, nome, data_aluguel):

        if not (self.is_alugado(nome)):
            return self.db.execute_query(
                'MATCH(p:Pessoa{email:$email}),(j:Jogo{nome:$nome}) CREATE (p)-[r:ALUGOU{'
                'data_aluguel:$data_aluguel}]->(j) RETURN r',
                {'email': email, 'data_aluguel': data_aluguel, 'nome': nome})
        else:
            print('O jogo ja foi alugado')

    def is_alugado(self, nome):
        aux = self.db.execute_query('MATCH (p:Pessoa)-[r:ALUGOU]->(j:Jogo{nome:$nome}) RETURN r',
                                    {'nome': nome})
        return len(aux) != 0

    def ver_jogos(self):
        return self.db.execute_query('MATCH (j:Jogo) WHERE NOT ()-[:ALUGOU]->(j) RETURN j.nome as `Jogos`')

    def devolver_jogo(self, email, nome):
        return self.db.execute_query(
            'MATCH(p:Pessoa{email:$email})-[r:ALUGOU]->(j:Jogo{nome:$nome}) DELETE r',
            {'email': email, 'nome': nome})
