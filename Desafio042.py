#Refaça o desafio035 dos triangulos, acrescentando o recurso de mostrar qual tipo de triangulo sera formado:
#Equilatero: todos os lados iguais
#Isósceles: Dois lados iguais
#Escaleno: Todos os lados diferentes
print('=+/' * 8)
print('ANALISADOR DE TRIÂNGULOS')
print('=+/' * 8)
r1 = float(input('\nPrimeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Os tres valores digitados fecham um triangulo do tipo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO (todos os lados iguais)')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES (dois lados iguais)')
    else:
        print('ESCALENO (todos os lados diferentes)')
else:
    print('Os valores informados não fecham um triangulo')
