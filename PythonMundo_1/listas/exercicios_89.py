ficha = list()

while True: 
    nome = str(input('nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])
    
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break


print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')