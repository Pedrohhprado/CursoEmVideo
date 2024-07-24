num = int(input('leia um numero e veja o seu fatorial:'))
c = num
f = 1

while c>0:
    print('{}'.format(c),end=(''))
    print(' x ' if c > 1 else ' =', end=(''))
    f*=c
    c-=1

print('' ,f)