primeira_nota = float(input('Primeira nota: '))
segunda_nota = float(input('Segunda nota: '))

media = (primeira_nota + segunda_nota) / 2
print('Tirando {} e {}, a media do aluno sera {}'.format(primeira_nota, segunda_nota, media))

if media < 5.0:
    print("O aluno esta reprovado")
elif media >= 5 and media < 7:
    print('O aluno esta em recuperação')
else:
    print('o aluno esta aprovado')