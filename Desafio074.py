#Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estão na tupla.
from random import randrange
tupla = (randrange(0, 11), randrange(0, 11), randrange(0, 11), randrange(0, 11))
print(f'Os numeros gerados aleatoriamente são: {tupla}')
print(f'O menor numero {min(tupla)}')
print(f'O maior numero {max(tupla)}')
