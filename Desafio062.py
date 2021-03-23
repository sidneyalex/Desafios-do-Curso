#Melhore o Desafio061, perguntando para o usuario se ele quer mostrar mais alguns termos. O pgm encerra quando ele disser que quer mostrar 0 termos.
from time import sleep
c = 0
fim = False
print('{:=^50}'.format(' Prograssão Aritmética '))
num = int(input('\nDigite o 1º termo da P.A.: '))
quant = int(input('Quantos termos? '))
razão = int(input('Qual a razão? '))
while fim == False:
    while c != quant:
        print('{}'.format(num), end='')
        print(' - ' if c < quant - 1 else '', end='')
        num += razão
        c += 1
    c = 0
    quant = int(input('\nMais termos? (Senão digite 0) '))
    if quant == 0:
        fim = True
