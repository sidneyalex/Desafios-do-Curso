#Crie um pgm onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
#Caso o numero ja exista la dentro, ele não será adicionado.
#No final, serão exibidos todos os valores unicos digitados, em ordem crescente.
listanum = list()
while True:
    num = int(input('Qual numero deseja incluir na lista? '))
    if num not in listanum:
#    if listanum.count(num) == 0:
        listanum.append(num)
        print(f'Numero {num} adicionado a lista.')
    else:
        print(f'Numero ja adicionado anteriomente. Tente outro numero.')
    maisnum = ' '
    while maisnum not in 'sn':
        maisnum = str(input('Deseja incluir mais numeros a lista? (S/N) ')).strip().lower()
        if maisnum not in 'sn':
            print('OPÇÃO INVÁLIDA...')
    if maisnum in 'n':
        break
listanum.sort()
print(f'\nOs numeros digitados, em ordem crescente: {listanum}')
print('{:=^40}'.format(' FIM DO PROGRAMA '))
