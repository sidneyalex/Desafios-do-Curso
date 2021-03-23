#Refaça o Desafio051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da prograssão usando a estrutura while.
c = 0
print('{:=^50}'.format(' Prograssão Aritmética '))
num = int(input('\nDigite o 1º termo da P.A.: '))
razão = int(input('Digite a razão: '))
print('Os 10 primeiros termos dessa progressão: | ', end='')
while c != 10:
    print('{} | '.format(num), end='')
    num += razão
    c += 1
