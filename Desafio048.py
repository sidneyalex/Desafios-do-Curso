#Faça um pgm q calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500.
somamult = 0
soma = 0
imp = 0
mult = 0
for numero in range(1, 501, 2):
    imp += + 1
    soma += numero
    if numero % 3 == 0:
        mult += + 1
        somamult += numero
print('Entre 1 e 500, temos {} numeros impares e {} multiplos de 3'.format(imp, mult))
print('A soma de todos os impares é {}'.format(soma))
print('A soma de todos os multiplos de 3 é {}'.format(somamult))
