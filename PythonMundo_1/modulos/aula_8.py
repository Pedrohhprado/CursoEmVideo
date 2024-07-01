import math

num = int(input('digite um numero:'))

raiz = math.sqrt(num)

print('a raiz de {} é {:.2f}'.format(num, math.ceil(raiz)))