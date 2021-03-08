#Crie um pgm que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Digite seu nome inteiro: ').strip()
nome = nome.upper()
quebrado = nome.split()
print('Você tem Silva no nome? {}'.format('SILVA' in quebrado))
