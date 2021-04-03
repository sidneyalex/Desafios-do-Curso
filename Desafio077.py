#Crie um pgm q tenha uma tupla com varias palavras(não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ('Palavras', 'Aleatorias', 'escolhidas', 'sem', 'nada', 'em', 'comum')
for p in tupla:
    print(f'\nNa palavra {p} temos as seguintes vogais: ', end='')
    for v in p:
        if v.lower() in 'aeiou':
            print(v, end='')
