#Crei um pgm que tenha uma tupla totalmente preenchida com uma contagem por
# extenso, de zero até vinte.
#Seu pgm deverá ler um numero pelo teclado(entre 0 e 20) e mostra-lo por
#extenso.
contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
    'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
    'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
stop = ' '
while stop not in 'n':
    while True:
        ent = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= ent <= 20:
            break
    print(f'O numero digitado foi {contagem[ent]}')
    stop = ' '
    while stop not in 'sn':
        stop = str(input('Deseja continuar? (S/N) ')).strip().lower()
