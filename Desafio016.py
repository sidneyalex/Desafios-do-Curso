#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from emoji import emojize
from math import trunc
num = float(input('Digite um número: '))
print('A porção inteira de {} é {}.'.format(num, trunc(num)))
print('Utilizando int a porção é {}.'.format(int(num)))
print(emojize('Mais um desafio feito :sunglasses:', use_aliases=True))
