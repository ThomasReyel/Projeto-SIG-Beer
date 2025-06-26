# Assinante (Id, Nome, contato (email), endereço)
# Assinatura (ID, Id(Assinante), id(plano))
# Planos (id, Id(Produto), preço, tempo)
# produto (id, nome do produto, tipo)

#Funcionamento:
# Módulo de assinante (Cadastro, assinar, checar assinatura, alterar assinatura, cancelar assinatura)
# Módulo do Admin (Criar planos, alterar Planos, checar assinaturas, cancelar tudo)
# Projeto Sig-Beer: Um Sistema de Assinatura de Cervejas
import admin
import cliente
cntrl_resp_global = 0
while cntrl_resp_global == 0:
    print("________________________________________________")
    print("|                                              |")
    print("| Olá, seja bem-vindo ao Sig-Beer!             |")
    print("| Qual módulo deseja entrar?                   |")
    print("|                                              |")
    print("| 1 - Cliente                                  |")
    print("| 2 - Admin                                    |")
    print("| 3 - Sair                                     |")
    print("|                                              |")
    aux = (input('| Digite aqui: '))
    print("|______________________________________________|")

    match aux:
        case '1':
            cliente.modclient()
        case '2':     
           admin.modadmin()
        case '3':
            print('\nVolte sempre!')
            cntrl_resp_global = 1
        case _:
            print('\nVocê não digitou uma opção válida, tente novamente')