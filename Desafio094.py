#Crie um pgm que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionario e todos os dicionários em uma lista. No final, mostre:
#A)Quantas pessoas foram cadastradas
#B)A média de idade do grupo
#C)Uma lista com todas as mulheres.
#D)Uma lista com todas as pessoas com idade acima da média.
cad = list()
dados = dict()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).strip()
    while True:
        dados['sexo'] = input('Sexo (M/F): ').strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
    dados['idade'] = int(input('Idade: '))
    cad.append(dados.copy())
    while True:
        continuar = str(input('Continuar (S/N)? ')).strip().lower()[0]
        if continuar in 'sn':
            break
    if continuar == 'n':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(cad)} pessoas.')
soma = 0
mulheres = list()
acima = list()
for v in range(0, len(cad)):
    soma += cad[v]['idade']
    if cad[v]['sexo'] == 'F':
        mulheres.append(cad[v]['nome'])
media = soma / len(cad)
print(f'A média de idade do grupo é {media:.0f}')
print(f'Lista das mulheres cadastradas: {mulheres}')
print('Lista com aqueles com idade acima da média: ')
for p in cad:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print()
