import math

c1 = float(input('comprimento do cateto oposto: '))
c2 = float(input('comprimento do cateto adjacente: '))

hipotenusa = math.sqrt(pow(c1,2) + pow(c2,2))

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))