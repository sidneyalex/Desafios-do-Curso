#Faça um pgm q leia três num e mostre qual é o maior e qual é o menor.
print('Vou te mostrar qual o menor e maior valor entre três que você digitar')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
if n1 > n2 and n1 > n3:
    print('O maior numero digitado foi {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior numero digitado foi {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('O maior numero digitado foi {}'.format(n3))
if n1 < n2 and n1 < n3:
    print('O menor numero digitado foi {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor numero digitado foi {}'.format(n2))
if n3 < n1 and n3 < n2:
    print('O menor numero digitado foi {}'.format(n3))
