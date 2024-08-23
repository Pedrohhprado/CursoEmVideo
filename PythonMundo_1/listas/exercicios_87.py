matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = soma_coluna = maior_valor = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'digite um valor para [{l} {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')

    print()

print('='*30)

print(soma)

print('='*30)

for l in range(0,3):
    soma_coluna += matriz[l][2]
print(soma_coluna)

print('='*30)

for c in range(0,3):
    if matriz[1][c] > maior_valor:
        maior_valor = matriz[1][c]

print(maior_valor)

        
    
