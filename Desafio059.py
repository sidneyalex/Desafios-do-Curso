#Crie um pgm que leia dois valores e mostre um menu na tela:
'''[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa'''
#seu pgm deverá realizar a operação solicitada em cada caso
from time import sleep
opção = 0
n1 = int(input('1º VALOR: '))
n2 = int(input('2ª VALOR: '))
while opção != 5:
    print('''\
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos numeros
    [5]sair do programa''')
    opção = int(input('Digite aqui sua opção: '))
    if opção == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opção == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif opção == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1< n2:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('Os dois valores são IGUAIS')
    elif opção == 4:
        n1 = int(input('1º VALOR: '))
        n2 = int(input('2ª VALOR: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
    print('=-'*15)
    sleep(2)
print('FIM')
