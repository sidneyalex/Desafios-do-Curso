#Faça um pgm que leia um numero qualquer e mostre seu fatorial.Ex: 5! = 5x4x3x2x1 = 120
n = int(input('Digite um número: '))
fatorial = 1
print('Calculando {}! = '.format(n), end='')
#Solução com while
'''contador = n
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1'''
#Fim da solução com while
#Solução com for
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
#Fim da solução com for
print(fatorial)
