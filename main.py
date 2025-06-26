# Assinante (Id, Nome, contato (email), endereço)
# Assinatura (ID, Id(Assinante), id(plano))
# Planos (id, Id(Produto), preço, tempo)
# produto (id, nome do produto, tipo)

#Funcionamento:
# Módulo de assinante (Cadastro, assinar, checar assinatura, alterar assinatura, cancelar assinatura)
# Módulo do Admin (Criar planos, alterar Planos, checar assinaturas, cancelar tudo)
# Projeto Sig-Beer: Um Sistema de Assinatura de Cervejas
import os
cntrl_resp_global = 0
cntrl_resp_cli = 0
cntrl_resp_adm = 0

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
    aux = int(input('| Digite aqui: '))
    print("|______________________________________________|")

    match aux:
        case 1:
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
                aux = int(input('| Digite aqui: '))
                print("|_____________________________________________________________|")
                match aux:
                    case 1:
                        print("\n_____ Cadastrar Cliente _____\n")
                        nome = input("|Insira o seu nome: ")
                        email = input("|Insira o seu Email: ")
                        endereco = input("|Insira o seu endereço: ")
                        print("|Escolha entre um desses planos: \n|1 - Plano Mensal \n|2 - Plano Anual")
                        plano = int(input("|Escolha o plano: "))
                        print("\n_____ Cliente cadastrado com sucesso!  _____\n")
                    case 2:
                        print("\n_____ Checar Conta Cliente _____\n")
                        identificador = int(input("|Insira o seu ID: "))
                        print("|ID: ")
                        print("|Nome: ")
                        print("|Endereço: ")
                        print("|Email: ")
                        print("|Plano: ")
                    case 3:
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
                    case 4:
                        print("\n_____ Cancelar Assinatura Cliente _____\n")
                        identificador = int(input("Insira o seu ID: "))
                        print("\n_____ Conta Excluída com sucesso com sucesso!  _____\n")               
                    case 5:
                        cntrl_resp_cli = 1 
                    case _:
                        print('\nVocê não digitou uma opção válida, tente novamente')
            cntrl_resp_cli = 0 
        case 2:     
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
                aux = int(input('| Digite aqui: '))
                print("|_____________________________________________________________|")
                match aux:
                    case 1:
                        print("\n_____ Cadastrar Plano _____\n")
                        nome = input("|Insira o nome do plano: ")
                        produtoID = input("|Insira o ID do produto: ")
                        tempo = input("|Insira período do plano: ")
                        print("\n_____ Plano cadastrado com sucesso!  _____\n")
                    case 2:
                        print("\n_____ Checar Planos _____\n")
                        print("|Plano: ")
                        print("| - Produtos: ")
                        print("| - Período")
                    case 3:
                        print("\n_____ Checar Produtos _____\n")
                        print('|Id: 01 - Nome: Grama douroda - Tipo: Ale')
                    case 4:
                        print("\n_____ Alterar Planos _____\n")
                        input('|insira o ID do plano: ')
                        print("|Nome atual do plano: ")
                        print("|Produtos atuais do plano: ")
                        print("|Período atual do plano: ")
                        print("\n_____ Plano Alterado com sucesso!  _____\n")
                    case 5:
                        print("\n_____ Excluir Planos _____\n")
                        input('|insira o ID do plano: ')
                        print("\n_____ Conta Excluída com sucesso com sucesso!  _____\n")
                    case 6:
                        cntrl_resp_adm = 1 
                    case _:
                        print('\nVocê não digitou uma opção válida, tente novamente')
            cntrl_resp_adm = 0 
        case 3:
            print('\nVolte sempre!')
            cntrl_resp_global = 1
        case _:
            print('\nVocê não digitou uma opção válida, tente novamente')