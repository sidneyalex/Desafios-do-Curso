#Crie um pgm que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o pgm deverá perguntar se o usuario quer ou não continuar.
# No final, mostre:
# A)quantas pessoas tem mais de 18 anos.
# B)Quantos homens foram cadastrados.
# C)Quantas mulheres tem menos de 20 anos.
sexo = fim = ' '
maior = homens = moças = 0
print('Cadastros sem nome...\n')
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).strip().lower()
        if sexo == 'm':
            homens += 1
        else:
            if idade < 20:
                moças += 1
    while fim not in 'sn':
        fim = str(input('Continuar cadastros?(S/N) ')).strip().lower()
        print('='*20)
    if fim in 'n':
        break
    sexo = fim = ' '
print(f'ANALISANDO DADOS:')
print(f'\nPessoas com mais de 18 anos: {maior}\nQuantidade de homens cadastrados: {homens}\nMulheres com menos de 20: {moças}')
print('\n{} FIM DO PROGRAMA {}'.format('#'*5, '#'*5))
