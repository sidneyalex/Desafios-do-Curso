#Crie um pgm que leia o nome e o preço de varios produtos. O pgm deverá perguntar se o usúario vai continuar. No final, mostre:
# A)Qual é o total gasto na compra.
# B)Quantos produtos custam mais de R$1000
# C)Qual é o nome do produto mais barato.
print('='*18)
print('QUER PAGAR QUANTO?')
print('='*18)
total = maior = menor = 0
while True:
    produto = input('\nNome do Produto: ')
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        maior += 1
    if menor == 0 or preco < menor:
        menor = preco
        barato = produto
    fim = ' '
    while fim not in 'sn':
        fim = str(input('Continuar?(S/N) ')).strip().lower()[0]
    print('='*20)
    if fim == 'n':
        break
print(f'\nTotal da compra = {total:.2f}')
print(f'Sua lista tem {maior} produtos custando mais de MIL REAIS')
print(f'O produto mais barato da sua lista é {barato} custando R${menor:.2f}')
print('=' * 10, 'FIM DO PROGRAMA', '=' * 10)
