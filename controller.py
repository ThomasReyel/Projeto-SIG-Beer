def exibirprod(produto):
    for i in produto:
        print('| id: ',produto[i][0],' - Nome: ',produto[i][1],' - Tipo: ', produto[i][2])

def exibirplan(plano):
    for i in plano:
        print('| id: ',plano[i][0],' - Nome: ',plano[i][1],' - Ids dos produtos: ', plano[i][2],' - Preço: ',plano[i][3],' - Período: ',plano[i][4],' - Tempo de entrega: ',plano[i][5])

def cadastroplan(planos,identificadores, produto):
    iden = identificadores['plano']
    prod = []
    nome = input("|Insira o nome do plano: ")
    preco = float(input("|Insira o preço do plano: "))
    periodo = input("|Insira o periodo do plano: ")
    entrega = input("|Insira o tempo de entrega: ")
    print('|Esses são os produtos disponíveis: ')
    exibirprod(produto)
    aux = int(input('Quantos produtos vocês quer colocar: '))
    for i in range(aux):
        prod.append(int(input('insira os IDs')))
    planos.update({iden : [iden,nome,prod,preco,periodo,entrega]})
    identificadores['plano'] = iden+1  

def alterarplan(planos,identificador, produto):
    prod = []
    nome = input("|Insira o nome do plano: ")
    preco = float(input("|Insira o preço do plano: "))
    periodo = input("|Insira o periodo do plano: ")
    entrega = input("|Insira o tempo de entrega: ")
    print('|Esses são os produtos disponíveis: ')
    exibirprod(produto)
    aux = int(input('Quantos produtos vocês quer colocar: '))
    for i in range(aux):
        prod.append(int(input('insira os IDs')))
    planos[identificador] = [identificador,nome,prod,preco,periodo,entrega]