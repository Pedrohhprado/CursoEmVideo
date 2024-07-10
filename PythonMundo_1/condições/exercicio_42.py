r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r2:
    print('Os segmentos podem formar um triangulo')
    if r1 == r2 and r2 == r3:
        print('triangulo tipo: equilatero')
    elif r1 != r2 != r3:
        print('triangulo tipo: escaleno')
    else:
        print('triangulo tipo: isosceles')


else:
    print('os segmentos nao podem formar um triangulo')


