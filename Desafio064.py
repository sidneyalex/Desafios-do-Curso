#Crie um pgm que leia varios numeros inteiros pelo teclado. O pgm só vai parar quando o usr digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles(desconsiderando o flag'999')
num = int(input('Digite um numero: '))
soma = 0
c = 0
while num != 999:
    soma = soma + num
    c += 1
    num = int(input('outro numero [999 para SAIR]: '))
print('A soma dos {} numeros digitados é {}'.format(c, soma))
