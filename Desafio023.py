#Faça um pgm que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
#ex: Digite um numero:1834
#unidade:4
#dezena:3
#centena:8
#milhar:1
numero = input('Digite um numero de 0 a 9999: ')
dig = len(numero)
zeros = "0"*(4-dig)
total = zeros + numero
'''print('Unidade = {}'.format(total[-1]))
print('Dezena  = {}'.format(total[-2]))
print('Centena = {}'.format(total[-3]))
print('Milhar  = {}'.format(total[0]))'''
print('Unidade = {}\nDezena  = {}\nCentena = {}\nMilhar  = {}'.format(total[-1], total[-2], total[-3], total[0]))
