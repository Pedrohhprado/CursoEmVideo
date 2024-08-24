aluno = {'Nome':str(input('Nome: ')),
         'Media':float(input('Média: '))}

print(f'- nome é igual a {aluno['Nome']}')
print(f'- média é igual a {aluno['Media']}')
if aluno['Media'] >= 7:
    print(f'Situação do {aluno['Nome']} é igual a aprovado.')
else:
    print(f'Situação do {aluno['Nome']} é igual a reprovado.')
