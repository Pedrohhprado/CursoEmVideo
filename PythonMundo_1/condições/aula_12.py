# estrutura condicional aninhada

#exemplo
import random


print('escolha entre: pedra, papel e tesoura')
print('1- Pedra')
print('2- Papel')
print('3- tesoura')

escolha = int(input())
escolha_bot = random.randrange(1, 4)
escolhas=['', 'Pedra', 'papel', 'tesoura']

if escolha == escolha_bot:
    print('Empatou, os dois escolheram {}'.format(escolhas[escolha]))
elif escolha == 1 and escolha_bot == 3:
    print('voce ganhou, voce escolheu {} e o computador escolheu {}'.format(escolhas[escolha], escolhas[escolha_bot]))
elif escolha == 2 and escolha_bot == 1:
    print('voce ganhou, voce escolheu {} e o computador escolheu {}'.format(escolhas[escolha], escolhas[escolha_bot]))
elif escolha == 3 and escolha_bot == 2:
    print('voce ganhou, voce escolheu {} e o computador escolheu {}'.format(escolhas[escolha], escolhas[escolha_bot]))
elif escolha_bot== 1 and escolha == 3:
    print('voce perdeu, voce escolheu {} e o computador escolheu {}'.format(escolhas[escolha], escolhas[escolha_bot]))
elif escolha_bot == 2 and escolha == 1:
    print('voce perdeu, voce escolheu {} e o computador escolheu {}'.format(escolhas[escolha], escolhas[escolha_bot]))
elif escolha_bot == 3 and escolha == 2:
    print('voce perdeu, voce escolheu {} e o computador escolheu {}'.format(escolhas[escolha], escolhas[escolha_bot]))
else:
    print('numero invalido')


