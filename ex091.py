from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
for c in range(0, 4):
    sorteia_numeros = randint(1, 6)
    jogadores[f'Jogador{c + 1}'] = sorteia_numeros
ranking = []
print('Valores sorteados: ')
for key, value in jogadores.items():
    print(f'{key} tirou {value} no dado.')
    sleep(1)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)