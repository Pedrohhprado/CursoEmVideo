import random
numero = random.randrange(0,11)
cont = 1


print('Sou seu computador...')
print('Acabei de pensar um numero entre 0 e 10.')
print('Consegue adivinhar qual numero foi? ')
num = int(input('Qual o seu palpite? '))

while num != numero:
        if num > numero:
                print('Menos, tente mais uma vez.')
        else:
                print('Mais, tente mais uma vez.')
        num = int(input('Qual o seu palpite? '))
        cont = cont + 1

print('acertou com {} tentativas'.format(cont))

        