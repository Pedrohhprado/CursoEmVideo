num = list()

while True:
    
    n = int(input('Digite um valor: '))

    if n not in num:
        num.append(n)
        print('numero adicionado.')
    else:
        print('numero repetido, não sera adicionado.')

    opcao = str(input('deseja continuar?[S/N] '))
    if opcao in 'Nn':
        break
num.sort()
print(f'Os numeros adicionados foram : {num}')
