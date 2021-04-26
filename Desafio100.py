#Faça um pgm q tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep

def sorteia(lst):
    print('Sorteando 5 valores: ', end='',flush=True)
    sleep(1)
    cont = 0
    while cont < 5:
        numsort = randint(0, 10)
        if numsort not in lst:
            lst.append(numsort)
            cont += 1
            print(numsort, end=' ',flush=True)
            sleep(0.3)
    print()

def somapar(lst):
    soma = 0
    print(f'A soma dos valores pares: ', end='',flush=True)
    sleep(1)
    for v in lst:
        if v % 2 == 0:
            print(v, end=' ',flush=True)
            sleep(0.5)
            soma += v
    print(f'é {soma}\n')


numeros = list()
sorteia(numeros)
somapar(numeros)