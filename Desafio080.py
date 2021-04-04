#Crie um pgm onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if len(lista) == 0 or num >= lista[-1]:
        print('Valor adicionado ao final da lista')
        lista.append(num)
    else:
        p = 0
        for i, v in enumerate(lista):
            if v <= num:
                p = i + 1
        print(f'Valor adicionado a posição {p}')
        lista.insert(p,num)
print(f'{lista}')
