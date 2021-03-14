#A confederação Nacional de Natação precisa de um pgm q leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#até 9 anos: MIRIM
#até 14 anos: INFANTIL
#até 19 anos: JUNIOR
#até 25 anos: SÊNIOR
#acima: MASTER
from datetime import date
print('000' * 16)
print('0 \033[34;40mBEM VINDO A CONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m 0')
print('000' * 16)
nascimento = int(input('\nAtleta, digite o ano em que nasceu: '))
hoje = date.today().year
idade = hoje - nascimento
if idade <= 9:
    print('Com {} anos você está na categoria MIRIM, que vai até os 9 anos de idade.'.format(idade))
    print('Em {} anos você passa para a categoria INFANTIL, que vai até os 14.'.format(10 - idade))
elif idade <= 14:
    print('Com {} anos você está na categoria INFANTIL, que vai até os 14 anos de idade.'.format(idade))
    print('Em {} anos você passa para a categoria JUNIOR, que vai até os 19.'.format(15 - idade))
elif idade <= 19:
    print('Com {} anos você está na categoria JUNIOR, que vai até os 19 anos de idade.'.format(idade))
    print('Em {} anos você passa para a categoria SÊNIOR, que vai até os 20.'.format(20 - idade))
elif idade <= 25:
    print('Com {} anos você está na categoria SÊNIOR, que vai até os 20 anos de idade.')
    print('Em {} anos você passa para a categoria MASTER.'.format(26 - idade))
else:
    print('Você tem {} anos e está na categoria MASTER, parabéns pelo estilo de vida saudavel.'.format(idade))
