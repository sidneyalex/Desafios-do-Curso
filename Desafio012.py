#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('digite o preço do produto: R$'))
desc = preço * 0.05
print('O pruduto está com 5% de desconto, portanto voce economiza R${:.2f} e paga somente R${:.2f}.'.format(desc, preço - desc))
