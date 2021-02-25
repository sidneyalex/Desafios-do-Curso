#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
print('A média entra as notas {} e {} é {:.1f}'.format(n1, n2, (n1+n2)/2))
