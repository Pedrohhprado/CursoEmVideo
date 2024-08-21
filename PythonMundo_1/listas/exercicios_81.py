lista = []

while True:
    lista.append(int(input('Digite um Valor: ')))
    opcao = str(input('Dseja continuar?[S/N] '))
    if opcao in 'Nn':
        break

print(f'Voce digitou {len(lista)} valores.')
lista.sort(reverse=True)
print(f'os valores digitados em forma decrescente é: {lista}')
if 5 in lista:
    print('o numero 5 foi digitado')
else:
    print('o numero 5 nao foi digitado')