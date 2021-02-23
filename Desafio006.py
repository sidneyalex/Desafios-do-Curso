#Desafio 06 (Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.)
numero = int(input('Digite um numero inteiro: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print('O numero digitado foi ', numero)
print('Seu dobro = {} \nSeu triplo = {}'.format(dobro, triplo))
print('Sua Raiz quadrada é {:.2f}'.format(raiz))
