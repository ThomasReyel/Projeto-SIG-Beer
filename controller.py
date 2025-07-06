import datetime
def cadastroProd(produto, identificadores):
    iden = identificadores['produto']
    nome = input("|Insira o nome do produto: ")
    tipo = input("|Insira o tipo do produto: ")
    produto.update({iden : [iden,nome,tipo]})
    identificadores['produto'] = iden+1    

def alterarProd(produto):
    iden = int(input('|insira o ID do produto: '))
    if iden in produto:
        print("|Nome atual do produto: ", produto[iden][1])
        print("|Tipo atual do produto: ",produto[iden][2])
        nome = input('|Insira o novo nome: ')
        tipo = input('|Insira o novo tipo: ')
        produto[iden] = [iden,nome,tipo]
        print("\n_____ Produto Alterado com sucesso!  _____\n")
    else:
        print("\n|Esse produto não existe no banco de dados")

def exibirProd(produto):
    for i in produto:
        print('| id: ',produto[i][0],' - Nome: ',produto[i][1],' - Tipo: ', produto[i][2])

def deletarProd(produto):
    iden = int(input('|insira o ID do produto: '))
    if iden in produto:
        del produto[iden]
        print("\n_____ Conta Excluída com sucesso com sucesso!  _____\n")
    else: 
        print("\n| Produto não encontrado no Banco de dados")

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
    aux = int(input('insira quantos produtos vocês quer colocar: '))
    for i in range(aux):
        prod.append(int(input('| insira os IDs: ')))
    planos.update({iden : [iden,nome,prod,preco,periodo,entrega]})
    identificadores['plano'] = iden+1  

def alterarPlan(planos, produto):
    prod = []
    iden = int(input('|insira o ID do plano: '))
    if iden in planos:
        print("|Nome atual do plano: ", planos[iden][1])
        print("|Produtos atuais do plano: ", planos[iden][2])
        print('|Preço do plano atual: ',planos[iden][3])
        print("|Período atual do plano: ",planos[iden][4])
        print("|Tempo atual de entrega: ",planos[iden][5])
        nome = input("|Insira o nome do plano: ")
        preco = float(input("|Insira o preço do plano: "))
        periodo = input("|Insira o periodo do plano: ")
        entrega = input("|Insira o tempo de entrega: ")
        print('|Esses são os produtos disponíveis: ')
        exibirProd(produto)
        aux = int(input('Quantos produtos vocês quer colocar: '))
        for i in range(aux):
            prod.append(int(input('| insira os IDs: ')))
        planos[iden] = [iden,nome,prod,preco,periodo,entrega]
        print("\n_____ Plano Alterado com sucesso!  _____\n")
    else:
        print("\n|Esse plano não existe no banco de dados")

def deletarPlan(assinaturas, planos):
    iden = int(input('|insira o ID do plano: '))
    if iden in planos:
        del planos[iden]
        for i in assinaturas:
            if assinaturas[i][2] == iden:
                del assinaturas[i]
        print("\n_____ Conta Excluída com sucesso com sucesso!  _____\n")
    else:
        print("\n| Produto não encontrado no banco de dados")

def cadastrarCli(cliente,identificadores,planos, assinaturas):
    idenCli = identificadores['cliente']
    idenAs = identificadores['assinatura']
    nome = input("|Insira o nome do cliente: ")
    email = input("|Insira o email do cliente: ")
    endereco = input("|Insira o endereço do cliente: ")
    ano = int(input('|Insira o ano de Nascimento: '))
    mes = int(input('|Insira o mes de Nascimento: '))
    dia = int(input('|Insira o dia de Nascimento: '))
    data = datetime.date(ano,mes,dia)
    print('|Esses são os planos disponíveis: ')
    exibirPlan(planos)
    idPlano = int(input("|Insira o ID do plano do cliente: "))
    assinaturas.update({idenAs : [idenAs,idenCli,idPlano,datetime.date.today()]})
    cliente.update({idenCli : [idenCli,nome,email,endereco,data]})
    identificadores['cliente'] = idenCli+1
    identificadores['assinatura'] = idenAs+1      

def exibirCli(cliente):
    for i in cliente:
        print('| id: ',cliente[i][0],' - Nome: ',cliente[i][1],' - Email: ', cliente[i][2], ' - Endereço: ', cliente[i][3], ' - Data de Nascimento: ', cliente[i][4])

def alterarCli(cliente):
    iden = int(input('|insira o ID do cliente: '))
    if iden in cliente:
        print("|Nome atual do cliente: ", cliente[iden][1])
        print("|Email atual do cliente: ",cliente[iden][2])
        print("|Endereço atual do cliente: ",cliente[iden][3])
        print("|Data de nascimento atual do cliente: ",cliente[iden][4])
        nome = input('|Insira o novo nome: ')
        email = input('|Insira o novo email: ')
        endereco = input('|Insira o novo endereço: ')
        ano = int(input('|Insira o novo ano de Nascimento: '))
        mes = int(input('|Insira o novo mes de Nascimento: '))
        dia = int(input('|Insira o novo dia de Nascimento: '))
        data = datetime.date(ano,mes,dia)
        cliente[iden] = [iden,nome,email,endereco,data]
        print("\n_____ Conta atualizada com sucesso!  _____\n")
    else:
        print("\n|Esse cliente não existe no banco de dados")

def deletarCli(assinaturas, clientes):
    iden = int(input('|insira o ID do cliente: '))
    if iden in clientes:
        del clientes[iden]
        for i in range(len(assinaturas)):
            if assinaturas[i][1] == iden:
                del assinaturas[i]
        print("\n_____ Conta Excluída com sucesso com sucesso!  _____\n")  
    else:
        print("\n| Cliente não encontrado no banco de dados")

def cadastrarAss(assinaturas, identificadores):
    idenAs = identificadores['assinatura']
    idCli = int(input('| Insira o ID do cliente: '))
    idPlan = int(input('| Insira o ID do plano'))
    assinaturas.update({idenAs : [idenAs,idCli,idPlan,datetime.date.today()]})
    identificadores['assinatura'] = idenAs+1   
    
def exibirAss(assinaturas, clientes, planos):
    for i in assinaturas:
            print('| id: ',assinaturas[i][0],' - Cliente: ', clientes[assinaturas[i][1]][1],' - Plano: ', planos[assinaturas[i][2]][1], '- Data da Assinatura: ', assinaturas[i][3] )

def alterarAss(assinaturas, clientes, planos):
    iden = int(input('|insira o ID da assinatura: '))
    if iden in assinaturas:
        print('| Esse é o ID atual do Assinante:', assinaturas[iden][1], ' (', clientes[assinaturas[iden][1]][1] ,')')
        print('| Esse é o ID atual do Plano:', assinaturas[iden][2], ' (', planos[assinaturas[iden][2]][1] ,')')
        print('| Esse é a data atual da assinatura', assinaturas[iden][3])
        idCli = int(input('| Insira o no ID do cliente:'))
        idPlan = int(input('| Insira o no ID do plano:'))
        ano = int(input('|Insira o novo ano da assinatura: '))
        mes = int(input('|Insira o novo mes da assinatura: '))
        dia = int(input('|Insira o novo dia da assinatura: '))
        data = datetime.date(ano,mes,dia)
        assinaturas[iden] = [iden,idCli,idPlan,data]
        print("\n_____ assinatura Alterado com sucesso!  _____\n")

    else:
        print("\n|Essa Assinatura não existe no banco de dados")

def deletarAss(assinaturas):
    iden = int(input('|insira o ID da assinatura: '))
    if iden in assinaturas:
        del assinaturas[iden]
        print("\n_____ Conta Excluída com sucesso com sucesso!  _____\n")
    else:
        print("\n| Assinatura não encontrada")