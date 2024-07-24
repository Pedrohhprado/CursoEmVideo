primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 0
opcao = -1
cont_termos = 10

while cont<10:
    print('{}'.format(termo), end=(''))
    print(' -> ' if cont<9  else' -> Pausa',end=(''))
    termo += razão
    cont += 1
    if cont == 10:
        opcao = int(input('\nQuantos termos mais voce quer mostrar? '))
        if opcao != 0:
            cont -= opcao
        cont_termos += opcao
    else:
        cont == 11

print('Progressão finalizada com {} termos mostrados'.format(cont_termos))