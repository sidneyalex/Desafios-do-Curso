#Crie um pgm q vai ler varios numeros e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas valores pares e os valores impares digitados, respectivamente.
#No final mostre o conteudo das três listas geradas.
lista = []
listapar = []
listaimp = []
while True:
    lista.append(int(input('Digite um valor: ')))
    seg = ' '
    while seg not in 'sn':
        seg = str(input('Quer continuar? (S/N) ')).strip().lower()[0]
        if seg not in 'sn':
            print('OPÇÃO INVÁLIDA. DIGITE S OU N.')
    if seg == 'n':
        break
for p in lista:
    if p % 2 == 0:
        listapar.append(p)
    else:
        listaimp.append(p)
print(f'Lista Digitada: {lista}')
print(f'Par: {listapar}')
print(f'Impar: {listaimp}')
