##exemplos while

c=1

while c < 11:
   print(c)
   c= c + 1
print('Fim')

#usando if

num = 1

while num != 0:
    num1 = int(input('digite um numero: '))
    num = num1

    if num % 2==0 and num != 0:
        print('{} é par'.format(num))
    elif num==0:
        print('fim')
    else:
        print('{} é impar'.format(num))
