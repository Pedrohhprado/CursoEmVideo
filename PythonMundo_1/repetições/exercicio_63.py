num = int(input('quantos termos voce quer mostrar? '))
f1 = 1
f2 = 1
num -=3

print(('0 -> {} -> {} -> ').format(f1,f2),end='')
while num > 0:
    fn = f1+f2
    print('{}'.format(fn),end='')
    print(' -> ' if num > 1 else ' -> FIM', end='')
    
    f1 =f2
    f2 = fn
    num -= 1
    