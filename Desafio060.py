#Faça um pgm que leia um numero qualquer e mostre seu fatorial.Ex: 5! = 5x4x3x2x1 = 120
n = int(input('Digite um número: '))
fat = n
acumulado = n
total = fat
while fat != 1:
    print('{} '.format(fat), end='')
    fat = fat - 1
    acumulado = acumulado * fat
    if fat != 1:
        print('x ', end='')
    else:
        print('x 1 = ', end='')
print(acumulado)
