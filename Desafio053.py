#Crie um pgm q leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
'''APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA'''
frase = input('Digite uma frase: ').strip().upper()
cortado = frase.split()
junto = ''.join(cortado)
inv = ''
print('A Frase digitada: {}'.format(junto))
for ret in range(len(junto) - 1, -1, -1):
    inv += junto[ret]
print('A frase invertida: {}'.format(inv))
if junto == inv:
    print('É um PALINDROMO!')
else:
    print('Não é um PALINDROMO!')
