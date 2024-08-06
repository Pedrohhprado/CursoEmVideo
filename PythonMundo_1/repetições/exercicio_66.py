num = 0
cont = 0

while True:
    num = int(input('Digite um numero: '))
    if num == 999:
        break
    cont += num

print(cont)