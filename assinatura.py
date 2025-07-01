def modassin():
    cntrl_resp_assin = 0 
    while cntrl_resp_assin == 0:
            print("_______________________________________________________________")
            print("|                                                             |")
            print("| Olá, você entrou no módulo dos assinaturas                  |")
            print("| O que você deseja fazer?                                    |")
            print("| 1 - Checar assinaturas                                      |")
            print("| 2 - Alterar assinaturas                                     |")
            print("| 3 - Excluir assinaturas                                     |")
            print("| 4 - Voltar                                                  |")
            print("|                                                             |")
            aux = (input('| Digite aqui: '))
            print("|_____________________________________________________________|")
            match aux:
                case '1':
                    print("\n_____ Checar assinaturas _____\n")
                    print("|assinatura: ")
                    print("| - Produtos: ")
                    print("| - Período")
                case '2':
                    print("\n_____ Alterar assinaturas _____\n")
                    input('|insira o ID do assinatura: ')
                    print("|Nome atual do assinatura: ")
                    print("|Produtos atuais do assinatura: ")
                    print("|Período atual do assinatura: ")
                    print("|Tempo atual de entrega: ")
                    print("\n_____ assinatura Alterado com sucesso!  _____\n")
                case '3':
                    print("\n_____ Excluir assinaturas _____\n")
                    input('|insira o ID do assinatura: ')
                    print("\n_____ Conta Excluída com sucesso com sucesso!  _____\n")
                case '4':
                    cntrl_resp_assin = 1 
                case _:
                    print('\nVocê não digitou uma opção válida, tente novamente')
    cntrl_resp_assin = 0 