#Faça um pgm que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Que ano quer analizar? Digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano BISSEXTO.'.format(ano))
else:
    print('{} não é um ano BISSEXTO.'.format(ano))
