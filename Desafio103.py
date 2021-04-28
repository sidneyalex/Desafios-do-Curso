#Faça um pgm q tenha uma função chamada ficha(), q receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O pgm deverá ser capaz de mostrar a ficha do jogador, mesmo q algum dado não tenha sido informado corretamente.
def ficha(nome='<Não Informado>', gols='?'):
    return f'O jogador {nome} fez {gols} gol(s)'


jogador = str(input('Nome do jogador: ')).strip()
gol = str(input('Número de gols: ')).strip()
if jogador != '':
    if gol.isnumeric():
        gol = int(gol)
        print(ficha(jogador, gol))
    else:
        print(ficha(jogador))
else:
    if gol.isnumeric():
        gol = int(gol)
        print(ficha(gols=gol))
    else:
        print(ficha())
