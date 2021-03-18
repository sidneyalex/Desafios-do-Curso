#desenvolva um pgm q leia o 1º termo e a razão de uma PA(progressão aritmetica). No final, mostre os 10 primeiros termos dessa progressão.
num = int(input('Digite o 1º termo da P.A.: '))
razão = int(input('Digite a razão: '))
print('Os 10 primeiros termos dessa progressão: | ', end='')
for c in range(num, num + razão * 10, razão):
    print('{:2} |'.format(c), end=' ')
