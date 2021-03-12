#Escreva um pgm que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
print('Verifica maior valor entre 2 numeros.')
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O primeiro valor({}) é MAIOR.'.format(n1))
elif n1 < n2:
    print('O segundo valor({}) é MAIOR.'.format(n2))
else:
    print('Não existe valor MAIOR, os dois são IGUAIS.')
