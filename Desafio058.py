#Melhore o jogo do Desafio028 onde o computador vai "pensar" em um numero entre 0 e 10. Só que agr o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.
from emoji import emojize
from random import randrange
tentativas = 1
ale = randrange(0,11)
print('{}\n|| Jogo de ADIVINHAÇÃO ||\n{}\n'.format('='*25, '='*25))
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.\nSera que você consegue adivinhar qual foi?')
num = int(input('Qual é o seu palpite? '))
while num != ale:
    tentativas += 1
    if ale > num:
        print('Mais... Tente outro numero: ', end='')
    else:
        print('Menos... Tente outro numero: ', end='')
    num = int(input())
print('\nApós {} tentativas:'.format(tentativas))
print(emojize(':tada: Parabéns você GANHOU com {} tentativas :tada:'.format(tentativas), use_aliases=True))
