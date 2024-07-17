
idade_final=0
velho = 0
cont_mulher=0
nome_velho=''
for pessoa in range(1,5):
    print('-----{}ª PESSOA -----'.format(pessoa))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '.upper()))
    idade_final = idade_final + idade

    
    if pessoa==1:
        velho=idade
        nome_velho=nome
        
        
    else:
        if idade>velho:
            velho=idade
            nome_velho=nome
    
    if idade<20 and sexo=='F':
        cont_mulher = cont_mulher+1
        
media_idade = idade_final/4

print('A média de idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho,nome_velho))
print('Aotodo sao {} mulheres com menos de  20 anos.'.format(cont_mulher))



    