#Crie um pgm onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
#No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from operator import itemgetter
from time import sleep
jogo = dict()
for n in range(1, 5):
    jogo[f"Jogador {n}"] = randint(1, 6)
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('=-' * 30)
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('\n  === RANKING DOS JOGADORES ===')
sleep(1)
for i, v in enumerate(ranking):
    print(f'  {i + 1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)
