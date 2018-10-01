import math
with open('iris.data') as arq:
    dados = [line.split(',') for line in arq.readlines() if line.strip()]  # type: Any

def distancia(ponto1, ponto2):
    pontos = (((float(ponto1[0])-float(ponto2[0]))**2) + ((float(ponto1[1])-float(ponto2[1]))**2) + ((float(ponto1[2])-float(ponto2[2]))**2) + ((float(ponto1[3])-float(ponto2[3]))**2))
    return math.sqrt(pontos)


def aprendizagem(amostras):
    treino = []
    for k_setosa in range(0, 25):
        treino.append(amostras[k_setosa])
    for k_versicolor in range(50, 75):
        treino.append(amostras[k_versicolor])
    for k_virginica in range(100, 125):
        treino.append(amostras[k_virginica])
    return treino

def teste(amostras):
    teste = []
    for k_setosa in range(25, 50):
        teste.append([amostras[k_setosa][0], amostras[k_setosa][1], amostras[k_setosa][2], amostras[k_setosa][3], '?'])
    for k_versicolor in range(75, 100):
        teste.append(
            [amostras[k_versicolor][0], amostras[k_versicolor][1], amostras[k_versicolor][2], amostras[k_versicolor][3],
             '?'])
    for k_virginica in range(125, 150):
        teste.append(
            [amostras[k_virginica][0], amostras[k_virginica][1], amostras[k_virginica][2], amostras[k_virginica][3],
             '?'])
    return (teste)

def testeOriginal(amostras):
    teste = []
    for k_setosa in range(25, 50):
        teste.append(amostras[k_setosa])
    for k_versicolor in range(75, 100):
        teste.append(amostras[k_versicolor])
    for k_virginica in range(125, 150):
        teste.append(amostras[k_virginica])
    return (teste)


def contagem(lista,ponto):
    irisSetosa = 0
    irisVersicolor = 0
    irisVirginica = 0
    for k in range(len(lista)):
        if(lista[k][4] == 'Iris-setosa\n'):
            irisSetosa += 1
        elif(lista[k][4] == 'Iris-versicolor\n'):
            irisVersicolor += 1
        else:
            irisVirginica += 1
    if(irisVirginica > irisVersicolor and irisVirginica > irisSetosa):
        return 'Iris-virginica\n'
    if(irisSetosa > irisVirginica and irisSetosa > irisVersicolor):
        return 'Iris-setosa\n'
    if(irisVersicolor > irisSetosa and irisVersicolor > irisVirginica):
        return 'Iris-versicolor\n'
    if(irisVirginica == irisSetosa):
        return pontoMaisProximo(ponto)
    if(irisVirginica == irisVersicolor):
        return pontoMaisProximo(ponto)
    if(irisVersicolor == irisSetosa):
        return pontoMaisProximo(ponto)

def ordenar(lista , ponto):
    menor = distancia(lista[0],ponto)
    for k in range(len(lista)):
        i = k
        for i in range(len(lista)):
            if(distancia(lista[i],ponto) > distancia(lista[k],ponto)):
                temp = lista[k]
                lista[k] = lista[i]
                lista[i] = temp
    return lista

def pontoMaisProximo(dado):
    memoria = aprendizagem(dados)
    distanciaPonto = 9999999
    for i in range(len(memoria)):
        distanciaAtual = distancia(memoria[i], dado)
        if(distanciaAtual < distanciaPonto):
            dado[4] = memoria[i][4]
            distanciaPonto = distanciaAtual
    return dado[4]

def classificador(dados, vizinhos):
    baseDeDados = aprendizagem(dados)
    testes = teste(dados)
    for k in range(len(baseDeDados)):
        menorDistancia = 99999999
        lista= []
        for i in range(len(testes)):
            distanciaAtual = distancia(baseDeDados[i],testes[k])
            lista.append(baseDeDados[i])
        testes[k][4] = contagem((ordenar(lista,testes[k]))[0:vizinhos],testes[k])
    return testes

def avaliar(teste,classificado):
    acertos = 0
    for k in range(len(teste)):
        if teste[k][4] == classificado[k][4]:
            acertos += 1
    return acertos

name = int(input("Digite um K"))
classificado = classificador(dados,name)
teste =testeOriginal(dados)
treinamento = aprendizagem(dados)
acertos = avaliar(teste,classificado)

print("Total de treinamento: %d" % len(aprendizagem(dados)))
print("Total de testes: %d" % len(testeOriginal(dados)))
print("Total de acertos: %d" % acertos)
print("Porcentagem dos acertos: %.2f" % (100*acertos/len(testeOriginal(dados))))