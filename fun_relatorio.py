import datetime
from collections import Counter

def calcular_idade(data_nascimento):
    hoje = datetime.date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade


def calcular_faixa_etária(clientes):
    aux = [0,0,0,0]
    for i in clientes:
        aux1 = calcular_idade(clientes[i][4])
        if aux1 >= 18 and aux1 <= 20:
            aux[0] += 1
        elif aux1 > 20 and aux1 <= 30:
            aux[1] += 1
        elif aux1 > 30 and aux1 <= 40:
            aux[2] += 1
        elif aux1 > 40 and aux1 <= 50:
            aux[3] += 1
    print("|Temos clientes nas seguintes faixas etárias \n - Entre 18 e 20 anos: ",aux[0],"\n - Entre 20 e 30 anos: ",aux[1],"\n - Entre 30 e 40 anos: ",aux[2],"\n - Entre 40 e 50 anos: ",aux[3])

def calcular_planos_assinados(assinaturas, planos):
    elementos = [assinaturas[i][2] for i in assinaturas]
    contagem = Counter(elementos)
    id_mais_comum,quantidade = contagem.most_common(1)[0]
    print("O plano mais vendido é o: ", planos[id_mais_comum][1], 'Assinado ',quantidade,' vezes')

def calcular_quant_assinaturas(assinaturas,clientes,planos):
    aux = int(input('insira a ano: '))
    data = datetime.date(aux,1,1)
    for i in assinaturas:
        if data.year == assinaturas[i][3].year:
            print('| id: ',assinaturas[i][0],' - Cliente: ', clientes[assinaturas[i][1]][1],' - Plano: ', planos[assinaturas[i][2]][1], '- Data da Assinatura: ', assinaturas[i][3] )
