import controller
def modassin(assinaturas, clientes, planos, identificadores):
    cntrl_resp_assin = 0 
    while cntrl_resp_assin == 0:
            print("_______________________________________________________________")
            print("|                                                             |")
            print("| Olá, você entrou no módulo dos assinaturas                  |")
            print("| O que você deseja fazer?                                    |")
            print("| 1 - Cadastro de assinaturas                                 |")
            print("| 2 - Checar assinaturas                                      |")
            print("| 3 - Alterar assinaturas                                     |")
            print("| 4 - Excluir assinaturas                                     |")
            print("| 5 - Voltar                                                  |")
            print("|                                                             |")
            aux = (input('| Digite aqui: '))
            print("|_____________________________________________________________|")
            match aux:
                case '1':
                      print("\n_____ Cadastrar assinatura _____\n")
                      controller.cadastrarAss(assinaturas,identificadores)
                      print("\n_____ Assinatura cadastrada com sucesso!  _____\n")
                case '2':
                    print("\n_____ Checar assinaturas _____\n")
                    controller.exibirAss(assinaturas,clientes,planos)
                case '3':
                    print("\n_____ Alterar assinaturas _____\n")
                    controller.alterarAss(assinaturas,clientes,planos)
                case '4':
                    print("\n_____ Excluir assinaturas _____\n")
                    controller.deletarAss(assinaturas)
                case '5':
                    cntrl_resp_assin = 1 
                case _:
                    print('\nVocê não digitou uma opção válida, tente novamente')
    cntrl_resp_assin = 0 