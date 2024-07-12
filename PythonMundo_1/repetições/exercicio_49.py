n = int(input('escolha o numero para ver a tabuada:'))
ate = int(input('até o numero:'))

for c in range(0,ate):
    soma= n * c
    print('{} X {} = {}'.format(n,c,soma))
