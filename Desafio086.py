#Crie um pgm que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#   0  1  2
#0 00 01 02
#1 10 11 12
#2 20 21 22
#No final, mostre a matriz na tela, com a formatação correta.
#Condicoes animadas com (if, else, elif, or)
#solução1
'''matriz = [[], [], []]
for v in range(0,3):
    num = int(input(f'Valor para posição [0, {v}]: '))
    matriz[0].append(num)
for v in range(0, 3):
    num = int(input(f'Valor para posição [1, {v}]: '))
    matriz[1].append(num)
for v in range(0, 3):
    num = int(input(f'Valor para posição [2, {v}]: '))
    matriz[2].append(num)'''
#soluçao2
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Posição [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()