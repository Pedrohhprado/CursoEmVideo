print('-'* 40)
print(f'{"Listagem de preços":^40}')
print('-'* 40)

Listagem = ('Lapis', 1.80,
            'Borracha', 0.90,
            'Caderno', 19.90,
            'Caneta', 2.50,
            'Estojo', 9.90,
            'Apontador', 3.00)

for pos in range(0, len(Listagem)):
    if pos % 2 == 0:
        print(f'{Listagem[pos]:.<30}',end='')
    else:
        print(f'R$ {Listagem[pos]:<7.2f}')

print('-'* 40)

