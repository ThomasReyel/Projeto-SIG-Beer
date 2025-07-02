def cadastroProd(produto, identificadores):
    iden = identificadores['produto']
    nome = input("|Insira o nome do produto: ")
    tipo = input("|Insira o tipo do produto: ")
    produto.update({iden : [iden,nome,tipo]})
    identificadores['produto'] = iden+1    

def alterarProd(produto):
    iden = int(input('|insira o ID do produto: '))
    print("|Nome atual do produto: ", produto[iden][1])
    print("|Tipo atual do produto: ",produto[iden][2])
    nome = input('|Insira o novo nome: ')
    tipo = input('|Insira o novo tipo: ')
    produto[iden] = [iden,nome,tipo]

def exibirProd(produto):
    for i in produto:
        print('| id: ',produto[i][0],' - Nome: ',produto[i][1],' - Tipo: ', produto[i][2])

def exibirPlan(plano):
    for i in plano:
        print('| id: ',plano[i][0],' - Nome: ',plano[i][1],' - Ids dos produtos: ', plano[i][2],' - Preço: ',plano[i][3],' - Período: ',plano[i][4],' - Tempo de entrega: ',plano[i][5])

def cadastroPlan(planos,identificadores, produto):
    iden = identificadores['plano']
    prod = []
    nome = input("|Insira o nome do plano: ")
    preco = float(input("|Insira o preço do plano: "))
    periodo = input("|Insira o periodo do plano: ")
    entrega = input("|Insira o tempo de entrega: ")
    print('|Esses são os produtos disponíveis: ')
    exibirProd(produto)
    aux = int(input('Quantos produtos vocês quer colocar: '))
    for i in range(aux):
        prod.append(int(input('insira os IDs')))
    planos.update({iden : [iden,nome,prod,preco,periodo,entrega]})
    identificadores['plano'] = iden+1  

def alterarPlan(planos,identificador, produto):
    prod = []
    nome = input("|Insira o nome do plano: ")
    preco = float(input("|Insira o preço do plano: "))
    periodo = input("|Insira o periodo do plano: ")
    entrega = input("|Insira o tempo de entrega: ")
    print('|Esses são os produtos disponíveis: ')
    exibirProd(produto)
    aux = int(input('Quantos produtos vocês quer colocar: '))
    for i in range(aux):
        prod.append(int(input('insira os IDs')))
    planos[identificador] = [identificador,nome,prod,preco,periodo,entrega]

def cadastrarCli(cliente,identificadores,planos, assinaturas):
    idenCli = identificadores['cliente']
    idenAs = identificadores['assinatura']
    nome = input("|Insira o nome do cliente: ")
    email = input("|Insira o email do cliente: ")
    endereco = input("|Insira o endereço do cliente")
    print('|Esses são os planos disponíveis: ')
    exibirPlan(planos)
    idPlano = int(input("|Insira o ID do plano do cliente"))
    assinaturas.update({idenAs : [idenAs,idenCli,idPlano]})
    cliente.update({idenCli : [idenCli,nome,email,endereco]})
    identificadores['cliente'] = idenCli+1
    identificadores['assinatura'] = idenAs+1      

def exibirCli(cliente):
    for i in cliente:
        print('| id: ',cliente[i][0],' - Nome: ',cliente[i][1],' - Email: ', cliente[i][2], ' - Endereço: ', cliente[i][3])

def alterarCli(cliente):
    iden = int(input('|insira o ID do cliente: '))
    print("|Nome atual do cliente: ", cliente[iden][1])
    print("|Email atual do cliente: ",cliente[iden][2])
    print("|Endereço atual do cliente: ",cliente[iden][3])
    nome = input('|Insira o novo nome: ')
    email = input('|Insira o novo email: ')
    endereco = input('|Insira o novo endereço: ')
    cliente[iden] = [iden,nome,email,endereco]
    
def exibirAss(assinaturas, clientes, planos):
    for i in assinaturas:
        print('| id: ',assinaturas[i][0],' - Cliente: ', clientes[assinaturas[i][1]][1],' - Plano: ', planos[assinaturas[i][2]][1])

def alterarAss(assinaturas, clientes, planos):
    iden = int(input('|insira o ID da assinatura: '))
    print('| Esse é o ID atual do Assinante:', assinaturas[iden][1], ' (', clientes[assinaturas[iden][1]][1] ,')')
    print('| Esse é o ID atual do Plano:', assinaturas[iden][2], ' (', planos[assinaturas[iden][2]][1] ,')')
    idCli = int(input('| Insira o no ID do cliente:'))
    idPlan = int(input('| Insira o no ID do plano:'))
    assinaturas[iden] = [iden,idCli,idPlan]