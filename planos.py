def modplan():
    cntrl_resp_plan = 0 
    while cntrl_resp_plan == 0:
            print("_______________________________________________________________")
            print("|                                                             |")
            print("| Olá, você entrou no módulo dos planos                       |")
            print("| O que você deseja fazer?                                    |")
            print("| 1 - Cadastrar plano                                         |")
            print("| 2 - Checar planos                                           |")
            print("| 3 - Alterar planos                                          |")
            print("| 4 - Excluir planos                                          |")
            print("| 5 - Voltar                                                  |")
            print("|                                                             |")
            aux = (input('| Digite aqui: '))
            print("|_____________________________________________________________|")
            match aux:
                case '1':
                    print("\n_____ Cadastrar Plano _____\n")
                    nome = input("|Insira o nome do plano: ")
                    tempo = input("|Insira período do plano: ")
                    entrega = input("|Insira o tempo de entrega: ")
                    print("\n_____ Plano cadastrado com sucesso!  _____\n")
                case '2':
                    print("\n_____ Checar Planos _____\n")
                    print("|Plano: ")
                    print("| - Produtos: ")
                    print("| - Período")
                case '3':
                    print("\n_____ Alterar Planos _____\n")
                    input('|insira o ID do plano: ')
                    print("|Nome atual do plano: ")
                    print("|Produtos atuais do plano: ")
                    print("|Período atual do plano: ")
                    print("|Tempo atual de entrega: ")
                    print("\n_____ Plano Alterado com sucesso!  _____\n")
                case '4':
                    print("\n_____ Excluir Planos _____\n")
                    input('|insira o ID do plano: ')
                    print("\n_____ Conta Excluída com sucesso com sucesso!  _____\n")
                case '5':
                    cntrl_resp_plan = 1 
                case _:
                    print('\nVocê não digitou uma opção válida, tente novamente')
    cntrl_resp_plan = 0 