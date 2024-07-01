import random

n = int(input('escolha um numero: '))
n_aleatorio = random.randrange(6)

if n == n_aleatorio:
    print('Parabens!! voce ganhou! ')
else:
    print('Voce errou! eu pensei {} e nao {}'.format(n_aleatorio, n))
