# Assinante (Id, Nome, contato (email), endereço)
# Assinatura (ID, Id(Assinante), id(plano))
# Planos (id, Id(Produto), preço, tempo)
# produto (id, nome do produto, tipo)

#Funcionamento:
# Módulo de assinante (Cadastro, assinar, checar assinatura, alterar assinatura, cancelar assinatura)
# Módulo do Admin (Criar planos / produtos, alterar Planos/produtos, checar assinaturas, cancelar tudo)
# Projeto Sig-Beer: Um Sistema de Assinatura de Cervejas
cntrl_resp_global = 0
cntrl_resp_cli = 0
while cntrl_resp_global == 0:
    print("_______________________________________________________________")
    aux = int(input('Olá, seja bem-vindo ao Sig-Beer!\nQual módulo deseja entrar?\n1 - Cliente\n2 - Admin\n3 - Sair\nDigite aqui: '))
    match aux:
        case 1:
            while cntrl_resp_cli == 0:
                print('\n\n\n\n\n\n\n\n\n\n')
                print("_______________________________________________________________")
                print('Olá, você entrou no módulo de Cliente, o que você deseja fazer')
                aux = int(input('1 - Cadastrar\n2 - Checar conta\n3 - Alterar assinatura\n4 - Cancelar assinatura\n5 - Voltar'))
                match aux:
                    case 1:
                        ...
                    case 2:
                        ...
                    case 3:
                        ...
                    case 4:
                        ...
                    case 5:
                        ...
                    case _:
                        print('Você não digitou uma opção válida, tente novamente')

                
        case 2:
            print('\n\n\n\n\n\n\n\n\n\n')
            print("_______________________________________________________________")
            print('Olá, você entrou no módulo de Administrador, o que você deseja fazer')
        case 3:
            print('Volte sempre')
            cntrl_resp_global=1        
        case _:
            print('Você não digitou uma opção válida, tente novamente')