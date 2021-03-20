#Crie um pgm q leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores. 21 anos
from datetime import date
hj = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    usr1 = int(input('Ano de nascimento do usuario {}: '.format(c)))
    if hj - usr1 < 21:
        menor += 1
    else:
        maior += 1
print('Condiderando que aos 21 anos você atinge a maioridade.\nDos 7 usuarios {} atingiram a maioridade e {} ainda não.'.format(maior, menor))
