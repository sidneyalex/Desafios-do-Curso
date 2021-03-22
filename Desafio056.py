#Desenvolva um pgm q leia o nome, idade, e sexo de 4 pessoas. No final do pgm, mostre:
'''A média de idade do grupo.
Qual é o nome do homem mais velho.
Quantas mulheres tem menos de 20 anos.'''
media = 0
maisvelho = 0
jovensmulheres = 0
nomeold = ''
for entrada in range(1, 5):
    print('===== {}ª PESSOA ====='.format(entrada))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    media += idade
    if sexo in 'Mm' and idade >= maisvelho:
        maisvelho = idade
        if nomeold == '':
            nomeold = nome
        elif idade > maisvelho:
            nomeold = nome
        else:
            nomeold = nomeold + ', ' + nome
    elif sexo in 'Ff' and idade < 20:
        jovensmulheres += 1
print('\nMedia de idade: {}'.format(media // 4))
print('Mulheres com menos de 20: {}'.format(jovensmulheres))
print('Nome do(s) homem(s) mais velho(s): {}'.format(nomeold))
