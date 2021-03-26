#Crie um pgm q simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado(numero inteiro) e o pgm vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere q o caixa possui cedulas de R$50, R$20, R$10 e R$1.
print('='*40)
print('{:=^40}'.format(' BANCO "SEM DINHEIRO" '))
print('='*40)
saque = int(input('\nQual o valor a ser sacado? R$ '))
nota = 50
quant = 0
while True:
    if saque >= nota:
        saque -= nota
        quant += 1
    else:
        if quant > 0:
            print(f'{quant} notas de R${nota}')
        quant = 0
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        if saque == 0:
            break
#Solução 1
'''n50 = n20 = n10 = n1 = 0
while saque >= 50:
    n50 += 1
    saque -= 50
    if saque < 50:
        print(f'{n50} notas de R$50.00')
while saque >= 20:
    n20 += 1
    saque -= 20
    if saque < 20:
        print(f'{n20} notas de R$20.00')
while saque >= 10:
    n10 += 1
    saque -= 10
    if saque < 10:
        print(f'{n10} notas de R$10.00')
while saque >= 1:
    n1 += 1
    saque -= 1
    if saque < 1:
        print(f'{n1} notas de R$1.00')'''
