#Crie um pgm onde o usuario digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parêntese abertos e fechados na ordem correta.
expressao = str(input('Digite uma expressão: '))
valid = list()
for c in expressao:
    if c == '(':
        valid.append(c)
    elif c == ')':
        if len(valid) > 0:
            valid.pop()
        else:
            valid.append(')')
            break
if len(valid) == 0:
    print('Sua expressão é VALIDA.')
else:
    print(f'Sua expressão está INVALIDA.')
