#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é hora de se alistar
#Se ja passou do tempo do alistamento.
#Seu pgm tbm deverá mostrar o tempo q falta ou que passou do prazo
import datetime
ano = int(input('Digite o ano do seu nascimento: '))
date = datetime.date.today().year
idade = date - ano
if idade > 18:
    print('Ja se passaram {} anos do seu alistamento, pois você esta com {} anos.'.format(idade - 18, idade))
elif idade == 18:
    print('Voce deve se alistar este ano, pois completa 18.')
else:
    print('Voce ainda tem {} anos, vai se alistar daqui a {} anos.'.format(idade, 18 - idade))
