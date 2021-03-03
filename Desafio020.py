#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''from random import sample
a1 = input('Digite o nome de um dos alunos: ')
a2 = input('Mais um: ')
a3 = input('Outro: ')
a4 = input('O ultimo: ')
seq = [a1, a2, a3, a4]
#embaralhado = sample(seq,k=4)
print('A sequencia de apresentação é {}'.format(sample(seq,k=4)))'''
from random import shuffle
a1 = input('Digite o nome de um dos alunos: ')
a2 = input('Mais um: ')
a3 = input('Outro: ')
a4 = input('O ultimo: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print(lista)
