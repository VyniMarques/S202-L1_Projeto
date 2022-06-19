from pprintpp import pprint as pp
from classes.cliente import Cliente
from classes.funcionario import Funcionario
from classes.locadora import Locadora
from classes.jogo import Jogo


locadora = Locadora()
if not locadora.read_locadora():
    locadora.create_locadora('Locadora', 0, 5)


def view():
    funcionario = Funcionario()
    cliente = Cliente()
    jogo = Jogo()
    while 1:
        print("======================MENU======================")
        option1 = input('\n1. Funcionario \n2. Cliente\n3. Sair\n')
        if option1 == '1':
            while 1:
                print("======================Funcionario======================")
                option2 = input(
                    '1. Adicionar Funcionario \n2. Adicionar Jogo \n3. Deletar Jogo \n4. Adicionar Cliente \n5. '
                    'Alterar email do Cliente \n6. Deletar Cliente \n7. Deletar Funcionario \n8. Voltar\n')
                if option2 == '1':
                    print("======================Adicionar Funcionario======================")
                    nome = input('Nome do funcionario: ')
                    numero = input('Telefone do funcionario: ')
                    endereco = input('Endereço do funcionario: ')
                    email = input('Email do funcionario: ')
                    dataComecou = input('Data de contratação: ')
                    cargo = input('Cargo do funcionario: ')
                    funcionario.create_pessoa(nome, numero, endereco, email, dataComecou, cargo)
                elif option2 == '2':
                    print("======================Adicionar jogo======================")
                    nome = input('Nome do Jogo:')
                    datalancamento = input('Data de lançamento do Jogo: ')
                    desenvolvedora = input('Desenvolvedor do Jogo: ')
                    genero = input('Genero do Jogo: ')
                    jogoaux = {
                        'nome': nome,
                        'datalancamento': datalancamento,
                        'desenvolvedora': desenvolvedora,
                        'genero': genero
                    }
                    funcionario.adiciona_jogo(jogoaux)
                elif option2 == '3':
                    print("======================Deletar jogo======================")
                    nome = input('Nome do Jogo: ')
                    funcionario.deleta_jogo(nome)
                elif option2 == '4':
                    print("======================Adicionar Cliente======================")
                    nome = input('Nome do novo cliente: ')
                    numero = input('Telefone do novo cliente: ')
                    endereco = input('Endereço do novo cliente: ')
                    email = input('Email do novo cliente: ')
                    dataCriacao = input('Data de criação: ')
                    cliente.create_pessoa(nome, numero, endereco, email, 0, dataCriacao)
                elif option2 == '5':
                    print("======================Alterar Email do Cliente======================")
                    nome = input("Nome do cliente: ")
                    email = input("Novo email: ")
                    funcionario.emailCliente(nome, email)
                elif option2 == '6':
                    print("======================Deletar Cliente======================")
                    nome = input('Nome do Cliente: ')
                    funcionario.deleta_cliente(nome)
                elif option2 == '7':
                    print("======================Deletar Funcionario======================")
                    nome = input('Nome do Funcionario: ')
                    funcionario.deleta_funcionario(nome)
                else:
                    break
        elif option1 == '2':
            while 1:
                print("========================Cliente========================")
                option3 = input('1. Ver jogos disponiveis \n2. Alugar Jogo \n3. Devolver Jogo \n4. Voltar\n')
                if option3 == '1':
                    print("======================Jogos Disponiveis======================")
                    aux = jogo.ver_jogos()
                    pp(aux)
                elif option3 == '2':
                    print("======================Alugar Jogo======================")
                    email = input("Email do cliente: ")
                    nome = input("Nome do jogo: ")
                    data = input("Data de Aluguel: ")
                    cliente.alugar(email, nome, data)
                elif option3 == '3':
                    print("======================Devolver Jogo======================")
                    email = input("Email do cliente: ")
                    nome = input("Nome do jogo: ")
                    cliente.devolver(email, nome)
                else:
                    break
        else:
            break


view()
