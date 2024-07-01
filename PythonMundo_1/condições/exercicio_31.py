distancia = int(input())

menos_200 =  distancia * 0.50
mais_200 = distancia * 0.45

if distancia <= 200:
    print('o preço da sua passagem de {}Km é R${:.2f}'.format(distancia, menos_200))
else:
    print('o preço da sua passagem de {}Km é R${:.2f}'.format(distancia, mais_200))
