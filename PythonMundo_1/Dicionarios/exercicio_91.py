from random import randint
from operator import itemgetter

jogadores = {'jogador1':randint(0,6),
             'jogador2':randint(0,6),
             'jogador3':randint(0,6),
             'jogador4':randint(0,6),
             }

ranking = {}
cont = 1

for k,v in jogadores.items():
    print(f'{k} tirou {v} no dado.')

print('='*30)
print('='*5,'Valores sorteados', '='*5)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('='*5,'Ranking dos jogadores', '='*5)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')


