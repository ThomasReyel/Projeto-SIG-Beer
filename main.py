# Assinante (Id, Nome, contato (email), endereço)
# Assinatura (ID, Id(Assinante), id(plano))
# Planos (id, Id(Produto), preço, tempo)
# produto (id, nome do produto, tipo)

#Funcionamento:
# Módulo de assinante (Cadastro, assinar, checar assinatura, alterar assinatura, cancelar assinatura)
# Módulo do Admin (Criar planos, alterar Planos, checar assinaturas, cancelar tudo)
# Projeto Sig-Beer: Um Sistema de Assinatura de Cervejas
import plano
import cliente
import produtos
import assinatura

bdproduto = {
    0 : [ 0, 'Campo Dourado', 'Ale' ],
    1 : [ 1,'Campo vermelho', 'lager' ]
}
bdcliente = {
    0 : [0, 'Thomas Morais', 'thomas@gmail.com', 'Ouro Branco/RN']
}
bdplano = {
    0 : [0,'Plano semestral', [0,1], 50.0, '6 meses', '2 semanas']
}
bdassinatura = {
    0 : [0,0,0]
}
identificadores = {
    'produto' : 2,
    'assinatante' : 1,
    'plano' : 1,
    'assinatura' : 1
}
cntrl_resp_global = 0
while cntrl_resp_global == 0:
    print("________________________________________________")
    print("|                                              |")
    print("| Olá, seja bem-vindo ao Sig-Beer!             |")
    print("| Qual módulo deseja entrar?                   |")
    print("|                                              |")
    print("| 1 - Assinantes                               |")
    print("| 2 - Planos                                   |")
    print("| 3 - Produtos                                 |")
    print("| 4 - Assinatura                               |")
    print("| 5 - Sair                                     |")
    print("|                                              |")
    aux = (input('| Digite aqui: '))
    print("|______________________________________________|")

    match aux:
        case '1':
            cliente.modclient(bdcliente, identificadores)
        case '2':     
           plano.modplan(bdplano, identificadores, bdproduto)
        case '3':     
           produtos.modprod(bdproduto, identificadores)
        case '4':
            assinatura.modassin()
        case '5':
            print('\nVolte sempre!')
            cntrl_resp_global = 1
        case _:
            print('\nVocê não digitou uma opção válida, tente novamente')