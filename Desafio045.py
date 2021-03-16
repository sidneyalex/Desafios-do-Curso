#Crie um programa q faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
print('{:*^40}'.format(' JOKENPÔ '))
pedra = 1
papel = 2
tesoura = 3
pc = randint(1, 3)
print('''
[1] PEDRA
[2] PAPEL
[3] TESOURA
''')
usr = int(input('Digite a opção desejada: '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!\n')
if pc == 1:
    print('Computador jogou PEDRA')
elif pc == 2:
    print('Computador jogou PAPEL')
else:
    print('Computador jogou TESOURA')
if usr == 1:
    print('Você jogou PEDRA ')
    if pc == 1:
        print('EMPATE, tente novamente.')
    elif pc == 2:
        print('Você PERDEU.')
    else:
        print('Você GANHOU.')
elif usr == 2:
    print('Você jogou PAPEL ')
    if pc == 1:
        print('Você GANHOU.')
    elif pc == 2:
        print('EMPATE, tente novamente.')
    else:
        print('Você PERDEU.')
elif usr == 3:
    print('Você jogou TESOURA ')
    if pc == 1:
        print('Você PERDEU.')
    elif pc == 2:
        print('Você GANHOU.')
    else:
        print('EMPATE, tente novamente')
else:
    print('OPÇÃO INVÁLIDA. Tente novamente.')
