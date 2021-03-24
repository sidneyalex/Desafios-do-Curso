#Crie um pgm que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag)
cont = soma = 0
while True:
    num = int(input('Digite um numero [999 para PARAR]: '))
    if num == 999:
        print('{:=^40}'.format(' FIM DO PROGRAMA '))
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} numeros e a soma deles é {soma}')
