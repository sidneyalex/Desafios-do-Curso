#Crie um pgm onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.
lista = [[], []]
for v in range(1,8):
    num = int(input(f'{v}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print('-='*10)
print(f'Lista de PARES: {lista[0]}')
print(f'Lista de IMPARES: {lista[1]}')
