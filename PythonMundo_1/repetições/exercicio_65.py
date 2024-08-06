cont = 0
maior= 0
menor= 1000000000000
soma = 0

opcao = 's'


while opcao in 'sS':
    num = int(input('Digite um numero: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
    soma += num

    opcao = str(input('Quer continuar? [S/N]'))


print('Você digitou {} numeros e a media foi {:.2f}'.format(cont, soma/cont))
print('O maior numero digitado foi {} e o menor foi {}'.format(maior, menor))

