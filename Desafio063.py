#Escreva um pgm que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de Fibonacci. Ex: 0->1->1->2->3->5->8 
#Sempre começa com 0 e 1 depois vem 1 2 3 5 8
print('{:@^40}'.format(' Sequência de Fibonacci '))
n = int(input('Quantos valores da sequência você quer ver? '))
c = ant = soma = 0
atual = 1
while c < n:
    print(soma, end='')
    c += 1
    print(' - ' if c < n else '', end='')
    if soma == 0:
        soma += 1
    else:
        soma = ant + atual
        ant = atual
        atual = soma
