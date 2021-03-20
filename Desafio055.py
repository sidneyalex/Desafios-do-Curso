#Faça um pgm que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for pessoas in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: (Kg) '.format(pessoas)))
    if peso > maior:
        maior = peso
        if menor == 0:
            menor = peso
    elif peso < menor:
        menor = peso
if maior == menor:
    print('Os valores apresentados são IGUAIS')
else:
    print('Maior PESO: {:.1f}Kg'.format(maior))
    print('Menor PESO: {:.1f}Kg'.format(menor))
