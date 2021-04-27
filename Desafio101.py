#Crie um pgm q tenha uma Função chamada voto() q vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL(-18 ou +65) ou OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 18 or idade > 65:
        if idade < 16:
            print('VOTO NEGADO')
        else:
            print('VOTO OPCIONAL')
    else:
        print('VOTO OBRIGATÓRIO')


ano = int(input('Digite o ano de seu nascimento: '))
voto(ano)