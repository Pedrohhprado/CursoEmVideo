num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite um ultimo numero: ')),)

print(f'Voce digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)}')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)} posição')
else:
    print('O valor não foi digitado')
print('Os valores pares digitados foram: ', end='')

for n in num:
    if n % 2==0:
        print(n)