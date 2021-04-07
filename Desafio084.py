#Faça um pgm que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final mostre:
#A)Quantas pessoas foram cadastradas.
#B)uma listagem com as pessoas mais pesadas.
#C)Uma listagem com as pessoas mais leves.
dados = list()
cadastro = list()
maior = menor = 0
while True:
    print('-=' * 15)
    dados.append(str(input('Nome: ')).strip())
    dados.append(float(input('Peso: Kg ')))
    if len(cadastro) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    seguir = ' '
    while seguir not in 'sn':
        seguir = str(input('Continuar? (S/N)')).strip().lower()[0]
    if seguir in 'n':
        break

print('-=' * 15)
print(f'{len(cadastro)} Novos Cadastros.')
print(f'O maior peso cadastrado foi {maior}kg. De ', end='')
for p in cadastro:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso cadastrado foi {menor}Kg. De ', end='')
for p in cadastro:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()
