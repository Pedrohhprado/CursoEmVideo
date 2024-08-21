comp = []
par = []
impar = []

for c in range(0,7):
    num = int(input(f'digite o {c+1} valor: '))
    
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

comp.append(par[:])
comp.append(impar[:])
par.sort()
impar.sort()
comp.sort()

print(f'Os valores impares digitados foram {par}.')
print(f'Os valores impares digitados foram {impar}')
print(comp)
 