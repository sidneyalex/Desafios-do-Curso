#Faça um pgm que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra"A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').strip().lower()
print('\nForam digitadas {} vezes a letra "A"'.format(frase.count('a')))
print('ela aparece primeiro na posição {}\ne por ultimo na {}\n'.format(frase.find('a')+1, frase.rfind('a')+1))
