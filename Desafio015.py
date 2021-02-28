#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros você andou com ele? '))
total = km * 0.15 + dias * 60
print('=' * 80)
print('A diaria do carro é de R$60 e temos um adicional de R$0.15 por km.')
print('=' * 80)
print('Você tem uma divida de R${:.2f}\nDiarias R${}\nKm      R${:.2f}'.format(total, dias * 60, km * 0.15))
print('=' * 80)
