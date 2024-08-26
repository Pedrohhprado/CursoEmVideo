pessoas = {'nome':str(input('Nome: ')),
           'nascimento':int(input('Ano de nascimento: '))}



pessoas['Carteira']=int(input('Carteira de trabalho (0 se não tem):'))

if pessoas['Carteira'] != 0:
    pessoas['ano'] = int(input('Ano de contratação: '))
    pessoas['salario'] = int(input('Salario: R$ '))
    pessoas['aposentadoria'] =65 - (2024 - pessoas['ano'] ) 
else:
    del pessoas['Carteira']
    

for  k, i in pessoas.items():
    print(f'{k} com os valores de {i}')


