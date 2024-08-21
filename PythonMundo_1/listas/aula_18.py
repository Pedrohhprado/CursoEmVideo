pessoas = [['Pedro',23],['Rania',19],['Gabriela',27]]
galera = []
dado = []
menorde = maiorde = 0
print(pessoas[0][0]) ##Pedro
print(pessoas[1][1]) ##19
print(pessoas[2][0]) ##Gabriela
print(pessoas[1]) ##[Rania,19]

for p in range(0,3):
    dado.append(str(input('Digite o nome da pessoas:')))
    dado.append(int(input('Digite a idade da pessoas:')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1]>17:
        print(f'{p[0]} é maior de idade.')
        maiorde += 1
    else:
        print(f'{p[0]} é menor de idade')
        menorde +=1
    

print(galera)
print(f'{maiorde} são maiores de idade e {menorde} são menores de idade.')
