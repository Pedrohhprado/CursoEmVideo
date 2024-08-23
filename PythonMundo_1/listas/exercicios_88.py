from random import randint
from time import sleep

lista = []
opcao = (int(input('')))
for c in range(0,6):
    for l in range(0,6):
        if l not in lista:
            lista.append(randint(1,60))
        else:
            lista.append(randint(1,60))

    lista.sort()
    print(lista)
    lista.clear()
    sleep(1)

