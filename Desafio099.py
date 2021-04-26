#Faça um pgm q tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu pgm tem q analisar todos os valores e dizer qual deles é o maior.
def maior(*num):
    print('-=' * 30)
    print("Analisando os numeros: ", end='')
    if num == ():
        num = (0,)
    for i, n in enumerate(num):
        if i == 0:
            maior = n
        elif maior < n:
            maior = n
        print(f'{n} ', end='')
    print(f'   Maior número é {maior}')


maior(1, 2, 3)
maior(10, 7, 3)
maior(20, 30, 10)
maior(9)
maior()
