#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
al1 = input('Digite o nome de um dos alunos: ')
al2 = input('Digite o nome de mais um aluno: ')
al3 = input('Digite o nome de outro aluno: ')
al4 = input('Digite o nome do ultimo aluno: ')
Alunos = [al1, al2, al3, al4]
print('O aluno sorteado foi {}'.format(choice(Alunos)))
