#Faça um pgm que leia 5 valores e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
#Solução 1
"""valores = [int(input('1º Valor: ')),
            int(input('2º Valor: ')),
            int(input('3º Valor: ')),
            int(input('4º Valor: ')),
            int(input('5º Valor: '))]
for v in range(0, len(valores)):
    if v == 0:
        maior = menor = valores[v]
        pma = v
        pme = v
    elif valores[v] > maior:
        maior = valores[v]
        pma = v
    elif valores[v] < menor:
        menor = valores[v]
        pme = v
    elif valores[v] == maior:
        pma = [pma, v]
    elif valores[v] == menor:
        pme = [pme, v]
print(f'''\
Valores digitados: {valores}
Maior Valor: {maior} POSIÇÃO: {pma}
Menor Valor: {menor} POSIÇÃO: {pme}''')
"""
#Solução 2
listanum = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'\nVocê digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
