def modadmin():
    cntrl_resp_adm = 0 
    while cntrl_resp_adm == 0:
            print("_______________________________________________________________")
            print("|                                                             |")
            print("| Olá, você entrou no módulo de Administrador                 |")
            print("| O que você deseja fazer?                                    |")
            print("| 1 - Cadastrar plano                                         |")
            print("| 2 - Checar planos                                           |")
            print("| 3 - Checar produtos                                         |")
            print("| 4 - Alterar planos                                          |")
            print("| 5 - Excluir planos                                          |")
            print("| 6 - Voltar                                                  |")
            print("|                                                             |")
            aux = (input('| Digite aqui: '))
            print("|_____________________________________________________________|")
            match aux:
                case '1':
                    print("\n_____ Cadastrar Plano _____\n")
                    nome = input("|Insira o nome do plano: ")
                    produtoID = input("|Insira o ID do produto: ")
                    tempo = input("|Insira período do plano: ")
                    print("\n_____ Plano cadastrado com sucesso!  _____\n")
                case '2':
                    print("\n_____ Checar Planos _____\n")
                    print("|Plano: ")
                    print("| - Produtos: ")
                    print("| - Período")
                case '3':
                    print("\n_____ Checar Produtos _____\n")
                    print('|Id: 01 - Nome: Grama douroda - Tipo: Ale')
                case '4':
                    print("\n_____ Alterar Planos _____\n")
                    input('|insira o ID do plano: ')
                    print("|Nome atual do plano: ")
                    print("|Produtos atuais do plano: ")
                    print("|Período atual do plano: ")
                    print("\n_____ Plano Alterado com sucesso!  _____\n")
                case '5':
                    print("\n_____ Excluir Planos _____\n")
                    input('|insira o ID do plano: ')
                    print("\n_____ Conta Excluída com sucesso com sucesso!  _____\n")
                case '7':
                    cntrl_resp_adm = 1 
                case _:
                    print('\nVocê não digitou uma opção válida, tente novamente')
    cntrl_resp_adm = 0 