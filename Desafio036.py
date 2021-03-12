#escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O pgm vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo sera negado.
print('\033[33m=+=\033[m' * 11)
print('\033[32m!!! SIMULADOR DE EMPRESTIMO !!!\033[m')
print('\033[33m=+=\033[m' * 11, '\n')
valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salario: R$'))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = valor / (anos * 12)
if prestacao <= (salario * 0.3):
    print('\nO emprestimo sai por {} x R${:.2f}'.format(anos * 12, prestacao))
else:
    print('\nO emprestimo foi \033[1;37;41mNEGADO\033[m, pois a parcela de R${:.2f} excede os 30% do salario que é R${:.2f}.'.format(prestacao, salario * 0.3))
