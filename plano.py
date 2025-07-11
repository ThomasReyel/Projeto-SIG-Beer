import controller
def modplan(planos, identificadores, produto, assinaturas):
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
                    controller.cadastroPlan(planos, identificadores, produto)
                    print("\n_____ Plano cadastrado com sucesso!  _____\n")
                case '2':
                    print("\n_____ Checar Planos _____\n")
                    controller.exibirPlan(planos)
                case '3':
                    print("\n_____ Alterar Planos _____\n")
                    controller.alterarPlan(planos,produto)
                case '4':
                    print("\n_____ Excluir Planos _____\n")
                    controller.deletarPlan(assinaturas,planos) 
                case '5':
                    cntrl_resp_plan = 1 
                case _:
                    print('\nVocê não digitou uma opção válida, tente novamente')
    cntrl_resp_plan = 0 