#Faça um pgm q tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
#Seu pgm tem q realizar três contagens através da função criada:
# a)De 1 até 10, de 1 em 1
# b)De 10 até 0, de 2 em 2
# c)Uma contagem personalizada
from time import sleep
def contador(início, fim, passo):
    print('-='*20)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {início} a {fim} de {passo} em {passo}')
    sleep(2.5)
    cont = início
    if início < fim:
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += passo
    else:
        cont = início
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= passo
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print(f'Sua vez. Defina os valores da contagem:')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)
