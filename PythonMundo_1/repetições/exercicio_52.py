num  =  int(input('digite um  numero:'))
tot = 0

for  c  in range (1, num + 1):
    if  num  %  c ==0:
        print('\033[33m', end=(' '))
        tot +=1
    else:
        print('\033[31m', end=(' '))

    print('{}'.format(c),  end=(' '))

print('\n\033[mO  numero foi divisivel {} vezes'.format(tot))
if   tot==2:
    print('e  por  isso  ele é primo')
else:
    print('e por isso ele  não é primo')


