#Faça um pgm q leia o nome completo de uma pessoa, mostrando em seguida o 1º e o ultimo nome separadamente.
#Ex:Ana Maria de Souza
#Primeiro=Ana
#Ultimo=Souza
nome = input('Digite seu nome completo: ').strip()
lista = nome.split()
print('\nSeu primeiro nome é {}\nSeu ultimo nome é {}'.format(lista[0], lista[-1]))
