#escreva um pgm que leia um numero inteiro e peça para o usuario escolher qual será a base de conversão:
#1 para binario
#2 para octal
#3 para hexadecimal
num = int(input('Digite um numero: '))
print('1 BINARIO\n2 OCTAL\n3 HEXADECIMAL')
con = int(input('Digite o numero da opção de converssão desejada:'))
if con == 1:
    print('O numero {} em binario é {}'.format(num, bin(num)[2:]))
elif con == 2:
    print('O numero {} em octal é {}'.format(num, oct(num)[2:])) 
elif con == 3:
    print('O numero {} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida.')
