#Faça um pgm que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
from emoji import emojize
print(emojize(':clock10: ATENÇÃO PARA A CONTAGEM REGRESSIVA :clock2:', use_aliases=True))
start = input('Tecle ENTER para iniciar.')
for c in range(10, 0, -1):
    print('{:^14}'.format(c))
    sleep(1)
print(emojize(':fireworks: ZEROOOOO :fireworks:'))
