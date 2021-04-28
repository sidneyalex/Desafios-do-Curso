#Crie um pgm q tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python, só q fazendo a validação para aceitar apenas um valor numérico.
#n=leiaint('Digite um n')
def leiaint(msg):
    num = input(msg)
    while num.isnumeric() is False:
        print(f'ERRO! {num} não é um número inteiro válido.')
        num = input(msg)
    num = int(num)
    return num


n=leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
