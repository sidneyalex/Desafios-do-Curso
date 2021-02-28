#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Digite o valor do seu Salário: R$'))
aum = sal * 0.15
print('Seu salario teve aumento de 15% equivalentes a R${:.2f}. Portanto seu salário atual é R${:.2f}'.format(aum, sal + aum))
