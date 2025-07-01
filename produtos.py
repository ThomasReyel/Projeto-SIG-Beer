import os
import controller
def modprod(produto, identificadores):
    cntrl_resp_prod = 0 
    while cntrl_resp_prod == 0:
            print("_______________________________________________________________")
            print("|                                                             |")
            print("| Olá, você entrou no módulo dos produtos                     |")
            print("| O que você deseja fazer?                                    |")
            print("| 1 - Cadastrar produtos                                      |")
            print("| 2 - Checar produtos                                         |")
            print("| 3 - Alterar produtos                                        |")
            print("| 4 - Excluir produtos                                        |")
            print("| 5 - Voltar                                                  |")
            print("|                                                             |")
            aux = (input('| Digite aqui: '))
            print("|_____________________________________________________________|")
            match aux:
                case '1':
                    os.system('clear')
                    print("\n_____ Cadastrar Produto _____\n")
                    iden = identificadores['produto']
                    nome = input("|Insira o nome do produto: ")
                    tipo = input("|Insira o tipo do produto: ")
                    produto.update({iden : [iden,nome,tipo]})
                    identificadores['produto'] = iden+1                  
                    print("\n_____ produto cadastrado com sucesso!  _____\n")
                case '2':
                    os.system('clear')
                    print("\n_____ Checar Produtos _____\n")
                    controller.exibirprod(produto)
                case '3':
                    os.system('clear')
                    print("\n_____ Alterar Produtos _____\n")
                    iden = int(input('|insira o ID do produto: '))
                    print("|Nome atual do produto: ", produto[iden][1])
                    print("|Tipo atual do produto: ",produto[iden][2])
                    nome = input('|Insira o novo nome: ')
                    tipo = input('|Insira o novo tipo: ')
                    produto[iden] = [iden,nome,tipo]
                    print("\n_____ Produto Alterado com sucesso!  _____\n")
                case '4':
                    os.system('clear')
                    print("\n_____ Excluir Produtos _____\n")
                    iden = int(input('|insira o ID do produto: '))
                    del produto[iden]
                    print("\n_____ Conta Excluída com sucesso com sucesso!  _____\n")
                case '5':
                    os.system('clear')
                    cntrl_resp_prod = 1 
                case _:
                    os.system('clear')
                    print('\nVocê não digitou uma opção válida, tente novamente')
    cntrl_resp_prod = 0 