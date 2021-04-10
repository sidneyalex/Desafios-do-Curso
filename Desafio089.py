#Crie um pgm q leia nome e duas notas de varios alunos e guarde em uma lista composta. No final, mostre um boletim contendo a media de cada um e permita q o usuario possa mostrar as notas de cada aluno individualmente.
lista = list()
while True:
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota1: '))
    n2 = float(input('Nota2: '))
    media = (n1 + n2) / 2
    lista.append([nome, [n1, n2], media])
    parar = ' '
    while parar not in 'sn':
        parar = str(input('Cadastrar mais alunos? (S/N) ')).strip().lower()[0]
    if parar == 'n':
        break
print('=' * 25)
print('ID   ALUNO      MEDIA')
for i, a in enumerate(lista):
    print(f'{i:<4} {a[0]:<10} {a[2]}')
print('=' * 25)
aluno = ' '
while True:
    aluno = int(input('Para visualizar as notas de um aluno digite seu ID. Para encerrar 999: '))
    if aluno == 999:
        break
    if aluno <= len(lista) - 1:
        print(f'Aluno: {lista[aluno][0]} Notas: {lista[aluno][1]}')
print('{:=^40}'.format('FIM DO PROGRAMA'))
