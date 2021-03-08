#Crie um programa q faça o computador "pensar" em um numero inteiro entre 0 e 5 para o usuario tentar desconbrir qual foi o numero escolhido. O pgm deve escrever na tela se o usuario ganhou ou perdeu.
from emoji import emojize
from random import randrange
ale = randrange(0,6)
print('{}\nJogo de ADIVINHAÇÃO\n{}\n'.format('='*20, '='*20))
num = int(input(print('Digite um numero inteiro de 0 a 5: ')))
if num == ale:
    print(emojize('Parabens você GANHOU :tada::sunglasses::thumbsup::tada:', use_aliases=True))
else:
    print('O numero era {}, tente denovo.'.format(ale))
