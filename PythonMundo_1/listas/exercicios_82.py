lista = []
lista_par = []
lista_impar = []

while True:
    lista.append(int(input('Digite um Valor: ')))
    opcao = str(input('Dseja continuar?[S/N] '))
    if opcao in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)

print(lista)
print(lista_par)
print(lista_impar)
