#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual seu salario atual: R$'))
if salario > 1250.00:
    print('Você recebeu 10% de aumento. Seu salario agora é R${}'.format(salario + (salario * 0.10)))
else:
    print('Você recebeu 15% de aumento. Seu novo salario é R${}'.format(salario + (salario * 0.15)))
