#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
C = float(input('Digite a temperatura em graus Celsius: C°'))
F = C * 9 / 5 + 32
print('{} Graus Celsius corresponde a {:.2f} Graus Fahrenheit.'.format(C, F))
