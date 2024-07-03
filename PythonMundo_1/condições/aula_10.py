### Condição simples
tempo = int(input('quanto anos tem seu carro? '))

if tempo <=3:
    print('seu carro é novo')
elif tempo >=4 and tempo <=9:
    print('seu carro é seminovo')
else:
    
    print('seu carro é velho')

print('----------------------------------------------')


### condição simplificada

print('carro novo' if tempo <= 3 else 'carro velho')