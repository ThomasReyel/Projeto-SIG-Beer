def modclient():
    cntrl_resp_cli = 0
    while cntrl_resp_cli == 0:
        print("_______________________________________________________________")
        print("|                                                             |")
        print("| Olá, você entrou no módulo de Cliente!                      |")
        print("| O que você deseja fazer?                                    |")
        print("| 1 - Cadastrar                                               |")
        print("| 2 - Checar conta                                            |")
        print("| 3 - Alterar assinatura                                      |")
        print("| 4 - Cancelar assinatura                                     |")
        print("| 5 - Voltar                                                  |")
        print("|                                                             |")
        aux = (input('| Digite aqui: '))
        print("|_____________________________________________________________|")
        match aux:
            case '1':
                print("\n_____ Cadastrar Cliente _____\n")
                nome = input("|Insira o seu nome: ")
                email = input("|Insira o seu Email: ")
                endereco = input("|Insira o seu endereço: ")
                print("|Escolha entre um desses planos: \n|1 - Plano Mensal \n|2 - Plano Anual")
                plano = int(input("|Escolha o plano: "))
                print("\n_____ Cliente cadastrado com sucesso!  _____\n")
            case '2':
                print("\n_____ Checar Conta Cliente _____\n")
                identificador = int(input("|Insira o seu ID: "))
                print("|ID: ")
                print("|Nome: ")
                print("|Endereço: ")
                print("|Email: ")
                print("|Plano: ")
            case '3':
                print("\n_____ Alterar Assinatura Cliente _____\n")
                identificador = int(input("Insira o seu ID: "))
                print("|Nome atual: ")
                nome = input("|Insira o seu novo nome: ")
                print("|Endereço atual: ")
                endereco = input("|Insira o seu novo endereço: ")
                print("|Email atual: ")
                email = input("|Insira o seu novo Email: ")
                print("|Plano atual: ")
                print("|Escolha entre um desses planos: \n|1 - Plano Mensal \n|2 - Plano Anual")
                plano = int(input("|Escolha o novo plano: "))
                print("\n_____ Conta atualizada com sucesso!  _____\n")
            case '4':
                print("\n_____ Cancelar Assinatura Cliente _____\n")
                identificador = int(input("Insira o seu ID: "))
                print("\n_____ Conta Excluída com sucesso com sucesso!  _____\n")               
            case '5':
                cntrl_resp_cli = 1 
            case _:
                print('\nVocê não digitou uma opção válida, tente novamente')
    cntrl_resp_cli = 0 