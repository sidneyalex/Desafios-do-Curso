#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiusculas
#O nome com todas as letras minisculas
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome.
nome = input('Digite seu nome completo: ')
nome = nome.strip()
espaços = nome.count(' ')
caractotal = len(nome)
caracnome = caractotal - espaços
print('Maiusculo:', nome.upper())
print('Minusculo:', nome.lower())
print('Tem ao todo {} letras.'.format(caracnome))
prinome = (nome.split())
print('Dos quais {} são do primeiro nome.'.format(len(prinome[0])))
