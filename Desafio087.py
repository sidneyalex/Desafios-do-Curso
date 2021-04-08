#Aprimore o desafio086, mostrando no final:
#A)A soma de todos os valores pares digitados.
#B)A soma dos valores da terceira coluna.
#C)O Maior valor da segunda linha
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if l == 1:
            if maior == 0 or matriz[l][c] > maior:
                maior = matriz[l][c]
print()
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if c == 2:
            soma += matriz[l][c]
    print()
print(f'\nSoma dos pares = {pares}')
print(f'A soma da 3ª coluna: {soma}')
print(f'Maior valor da 2ª linha: {maior}')
