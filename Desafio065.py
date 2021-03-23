#Crie um pgm que leia varios numeros inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos. O pgm deve perguntar ao usr se ele quer ou não continuar a digitar valores.
continuar = 's'
contador = soma = media = maior = menor = 0
while continuar in 's':
    num = int(input('Digite um numero: '))
    if contador == 0:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    soma += num
    contador += 1
    continuar = str(input('Continuar[S/N]? ')).strip().lower()
    while continuar not in 'sn':
        continuar = str(input('Opção inválida. Continuar[S/N]? '))
media = soma / contador
print('Foram digitados {} valores.\nMédia= {}\nMaior= {}\nMenor= {}'.format(contador, media, maior, menor))
