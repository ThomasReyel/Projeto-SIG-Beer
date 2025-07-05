import controller
def modclient(clientes, identificadores, planos, assinaturas):
    cntrl_resp_cli = 0
    while cntrl_resp_cli == 0:
        print("_______________________________________________________________")
        print("|                                                             |")
        print("| Olá, você entrou no módulo de Cliente!                      |")
        print("| O que você deseja fazer?                                    |")
        print("| 1 - Cadastrar                                               |")
        print("| 2 - Checar conta                                            |")
        print("| 3 - Alterar Informações                                     |")
        print("| 4 - Excluir Cliente                                         |")
        print("| 5 - Voltar                                                  |")
        print("|                                                             |")
        aux = (input('| Digite aqui: '))
        print("|_____________________________________________________________|")
        match aux:
            case '1':
                print("\n_____ Cadastrar Cliente _____\n")
                controller.cadastrarCli(clientes,identificadores,planos,assinaturas)
                print("\n_____ Cliente cadastrado com sucesso!  _____\n")
            case '2':
                print("\n_____ Checar Conta Cliente _____\n")
                controller.exibirCli(clientes)
            case '3':
                print("\n_____ Alterar Assinatura Cliente _____\n")
                controller.alterarCli(clientes)
            case '4':
                print("\n_____ Cancelar Assinatura Cliente _____\n")
                controller.deletarCli(assinaturas, clientes)             
            case '5':
                cntrl_resp_cli = 1 
            case _:
                print('\nVocê não digitou uma opção válida, tente novamente')
    cntrl_resp_cli = 0 