
cont_maior = 0
cont_menor = 0
for c in range(0,7):
    ano= int(input('em que ano a {}ª nasceu?'.format(c+1)))
    
    if 2040-ano > 18:
        cont_maior += +1
    else:
        cont_menor += +1

print('ao todo tivemos {} pessoas maiores de idade'.format(cont_maior))
print('ao todo tivemos {} pessoas menores de idade'.format(cont_menor))