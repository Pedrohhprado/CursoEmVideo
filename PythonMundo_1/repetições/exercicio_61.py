primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 0

while cont<10:
    print('{}'.format(termo), end=(''))
    print(' -> ' if cont<9 else' -> Fim',end=(''))
    termo += razão
    cont += 1
