def modprod():
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
                    print("\n_____ Cadastrar Produto _____\n")
                    nome = input("|Insira o nome do produto: ")
                    tipo = input("|Insira o tipo do produto: ")
                    print("\n_____ produto cadastrado com sucesso!  _____\n")
                case '2':
                    print("\n_____ Checar Produtos _____\n")
                    print("|produto: ")
                    print("| - Produtos: ")
                    print("| - tipo")
                case '3':
                    print("\n_____ Alterar Produtos _____\n")
                    input('|insira o ID do produto: ')
                    print("|Nome atual do produto: ")
                    print("|Produtos atuais do produto: ")
                    print("|tipo atual do produto: ")
                    print("\n_____ Produto Alterado com sucesso!  _____\n")
                case '4':
                    print("\n_____ Excluir Produtos _____\n")
                    input('|insira o ID do produto: ')
                    print("\n_____ Conta Excluída com sucesso com sucesso!  _____\n")
                case '5':
                    cntrl_resp_prod = 1 
                case _:
                    print('\nVocê não digitou uma opção válida, tente novamente')
    cntrl_resp_prod = 0 