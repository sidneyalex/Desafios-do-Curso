#Desenvolva um pgm que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A)Quantas vezes apareceu o numero 9.
#B)Em que posição foi digitado o primeiro 3.
#C)Quais foram os numeros pares.
print(f'O Programa coleta 4 numeros inteiros e os guarda em uma tupla.')
num = (int(input('1º numero: ')),
    int(input('2º numero: ')),
    int(input('3º numero: ')),
    int(input('4º numero: ')))
print(f'Os Valores digitados foram: {num}')
print(f'O numero 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro 3 foi digitado na posição {num.index(3) + 1}')
else:
    print('O numero 3 não foi digitado.')
print(f'Os numeros pares digitados: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
