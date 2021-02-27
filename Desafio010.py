#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
r = float(input('Quanto de dinheiro tem na sua carteira? R$'))
d = (r / 5.60)
i = (d * 112)
print('Você pode comprar {:.2f} Dólares.'.format(d))
print('Com esses {:.2f}U$ você pode comprar {:.2f} Ienes.'.format(d, i))
