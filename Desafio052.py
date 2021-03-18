#Faça um pgm q leia um numero int e diga se ele é ou não um numero primo.
numero = int(input('Digite um numero: '))
div = 0
for test in range(1, numero + 1):
    if numero % test == 0:
        div += 1
        print('\033[m{}'.format(test), end=' ')
    else:
        print('\033[31m{}'.format(test), end=' ')
print('\nO numero {} foi divisivel {} vezes'.format(numero, div))
if div == 2:
    print('e por isso ele é PRIMO!')
else:
    print('e por isso ele NÂO é PRIMO!')
