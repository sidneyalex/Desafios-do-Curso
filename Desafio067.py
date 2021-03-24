#Faça um pgm q mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. O programa será interrompido quando o numero solicitado for negativo.
while True:
    num = int(input('Digite um numero para ver sua tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num * c}')
    print('{:=^20}'.format(''))
print('{:=^41}'.format(' FIM DO PROGRAMA '))
