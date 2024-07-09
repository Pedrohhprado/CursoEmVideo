from datetime import date

ano = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = ano - nasc
print('O atleta tem {} anos'.format(idade))

if idade < 10:
    print('Classificação: MIRIM')
elif idade > 9 and idade < 15:
    print('Classificação: INFANTIL')
elif idade > 14 and idade < 20:
    print('Classificação: JUNIOR')
elif idade > 19 and idade < 26:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
