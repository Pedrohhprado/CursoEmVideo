n = 0
while True:
    n = int(input('escolha o numero para ver a tabuada:'))
    if n < 0:
            break
    for c in range(0,11):
        soma= n * c
        print('{} X {} = {}'.format(n,c,soma))
print('Fim')
        
