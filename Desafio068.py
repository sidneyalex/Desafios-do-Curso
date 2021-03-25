#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('{}{}'.format('§~'*12, '§'))
print('§ JOGO DO PAR OU IMPAR! §')
print('{}{}'.format('§~'*12, '§'))
cont = 0
escj = ' '
while True:
    while escj not in 'pi':
        escj = str(input('\nPAR ou IMPAR? [P/I] ')).strip().lower()
    if escj == 'p':
        escj = 'PAR'
    else:
        escj = 'IMPAR'
    numj = int(input('Qual numero quer jogar? '))
    numc = randint(0, 10)
    soma = numj + numc
    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    print('='*25)
    print(f'Você: {numj} Computador: {numc}. A soma é {soma} DEU {result}')
    if result == escj:
        print('Você VENCEU!')
    else:
        print('Você PERDEU!')
        break
    print('Só paro quando eu ganhar. Vamos jogar novamente...')
    print('='*25)
    cont += 1
print(f'Você ganhou {cont} vezes consecutivas.')
print('=-=-=-=-=-=-=-= FIM DE JOGO =-=-=-=-=-=-=-=')
