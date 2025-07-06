import fun_relatorio
def modrel(planos, clientes, assinaturas):
    cntrl_resp_rel = 0 
    while cntrl_resp_rel == 0:
            print("_______________________________________________________________")
            print("|                                                             |")
            print("| Olá, você entrou no módulo dos relatórios                   |")
            print("| O que você deseja fazer?                                    |")
            print("| 1 - Faixa Etária dos clientes                               |")
            print("| 2 - Planos mais assinados                                   |")
            print("| 3 - Assinaturas por ano                                     |")
            print("| 4 - Voltar                                                  |")
            print("|                                                             |")
            aux = (input('| Digite aqui: '))
            print("|_____________________________________________________________|")
            match aux:
                case '1':
                    fun_relatorio.calcular_faixa_etária(clientes)
                case '2':
                    fun_relatorio.calcular_planos_assinados(assinaturas,planos)
                case '3':
                   fun_relatorio.calcular_quant_assinaturas(assinaturas,clientes,planos)
                case '4':
                    cntrl_resp_rel = 1 
                case _:
                    print('\nVocê não digitou uma opção válida, tente novamente')
    cntrl_resp_rel = 0 