numeros = []
cont = 0


for c in range(0,5):
    numeros.append(int(input(f'digite um valor a posição {cont}: ')))
    cont += 1

print(f'Voce digitou os valores {numeros}')
print(f'O menor valor digitado foi {min(numeros)}')
print(f'O maior valor digitado foi {max(numeros)}')