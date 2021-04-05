#Crie um pgm q vai ler varios numeros e colocar em uma lista. Depois disso, mostre:
#A) Quantos numeros foram digitados.
#B) A lista de valores, ordenados de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    fim = ' '
    while fim not in 'sn':
        fim = str(input('Deseja continuar? (S/N) ')).strip().lower()
    if fim == 'n':
        break
print('-=' * 10)
print(f'A lista digitada: {lista}')
print(f'Itens na lista = {len(lista)} ')
print(f'Lista decrescente = {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O primeiro valor 5 encontrado na lista esta na posição: {lista.index(5)}')
else:
    print(f'O valor 5 não foi encontrado na lista.')
