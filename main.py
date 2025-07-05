# Projeto Sig-Beer: Um Sistema de Assinatura de Cervejas
import plano
import cliente
import produtos
import assinatura
import pickle

bdprodutos = {
    0 : [ 0, 'Campo Dourado', 'Ale' ],
    1 : [ 1,'Campo vermelho', 'lager' ]
}
try:
  arq_produtos = open("banco_de_dados/produtos.dat", "rb")
  bdprodutos = pickle.load(arq_produtos)
except:
  arq_produtos = open("banco_de_dados/produtos.dat", "wb")
arq_produtos.close()

bdclientes = {0 : [0, 'Thomas Morais', 'thomas@gmail.com', 'Ouro Branco/RN']}
try:
  arq_clientes = open("banco_de_dados/clientes.dat", "rb")
  bdclientes = pickle.load(arq_clientes)
except:
  arq_clientes = open("banco_de_dados/clientes.dat", "wb")
arq_clientes.close()

bdplanos = {0 : [0,'Plano semestral', [0,1], 50.0, '6 meses', '2 semanas']}
try:
  arq_planos = open("banco_de_dados/planos.dat", "rb")
  bdplanos = pickle.load(arq_planos)
except:
  arq_planos = open("banco_de_dados/planos.dat", "wb")
arq_planos.close()

bdassinaturas = {
    # 1° é o id prório, 2° é do cliente 3° é do plano
    0 : [0,0,0]
}
try:
  arq_assinaturas = open("banco_de_dados/assinaturas.dat", "rb")
  bdassinaturas = pickle.load(arq_assinaturas)
except:
  arq_assinaturas = open("banco_de_dados/assinaturas.dat", "wb")
arq_assinaturas.close()

identificadores = {
    'produto' : 0,
    'cliente' : 0,
    'plano' : 0,
    'assinatura' : 0
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
            cliente.modclient(bdclientes, identificadores,bdplanos,bdassinaturas)
        case '2':     
           plano.modplan(bdplanos, identificadores, bdprodutos,bdassinaturas)
        case '3':     
           produtos.modprod(bdprodutos, identificadores)
        case '4':
            assinatura.modassin(bdassinaturas,bdclientes,bdplanos)
        case '5':
            print('\nVolte sempre!')
            cntrl_resp_global = 1
            arq_produtos = open("banco_de_dados/produtos.dat", "wb")
            pickle.dump(bdprodutos, arq_produtos)
            arq_produtos.close()

            arq_clientes = open("banco_de_dados/clientes.dat", "wb")
            pickle.dump(bdclientes, arq_clientes)
            arq_clientes.close()

            arq_planos = open("banco_de_dados/paarq_planos.dat", "wb")
            pickle.dump(bdplanos, arq_planos)
            arq_planos.close()

            arq_assinaturas = open("banco_de_dados/paarq_assinaturas.dat", "wb")
            pickle.dump(bdassinaturas, arq_assinaturas)
            arq_assinaturas.close()
        case _:
            print('\nVocê não digitou uma opção válida, tente novamente')