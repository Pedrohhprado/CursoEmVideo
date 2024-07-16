maior= 0
menor= 0

for p in range(0,5):
    peso = (int(input('qual o peso da {}ª pessoa: '.format(p+1))))
    if p==1:
        maior = peso
        menor = peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print('o mais pesado foi de {}kg e o menos pesado foi de {}kg'.format(maior,menor))