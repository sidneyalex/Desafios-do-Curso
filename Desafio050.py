#Desenvolva um pgm q leia seis numeros int e mostre a soma apenas daqueles q forem pares. Se o valor digitado for impar, desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º numero: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos {} numeros pares que foram digitados é {}'.format(cont, soma))
