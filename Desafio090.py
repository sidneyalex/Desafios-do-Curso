#Faça um pgm q leia nome e média de um aluno, guardando também a situação em um dicionário. 
#No final, mostre o conteúdo da estrutura na tela.
cad = {'nome': input('Nome do aluno: ')}
cad['media'] = float(input(f'Qual a média de {cad["nome"]}? '))
if cad['media'] >= 7:
    cad['situação'] = 'Aprovado'
else:
    cad['situação'] = 'Reprovado'
print('=-'*25)
for i, v in cad.items():
    print(f' - {i} é igual a {v}')