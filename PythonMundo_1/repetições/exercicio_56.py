
idade_final=0
velho = 0
nome_mais_velho=''

for pessoa in range(1,5):
    print('-----{}ª PESSOA -----'.format(pessoa))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    #sexo = str(input('Sexo [M/F]: '))
    idade_final = idade_final + idade

    ##mais velho
    if pessoa==1:
        velho==idade
        
    else:
        if idade>velho:
            nome=idade
            


media_idade = idade_final/4
print('A média de idade do grupo é de {} anos.'.format(media_idade))
print(velho, nome)

    