#Aprimore o Desafio093 para q ele funcione com varios jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
cadgeral = list()
while True:
    cad = {'Nome': str(input('Nome do jogador: '))}
    partidas = int(input(f'Quantas partidas {cad["Nome"]} jogou? '))
    gols = list()
    for g in range(0, partidas):
        gols.append(int(input(f'Gols na partida {g + 1}: ')))
    cad['Gols'] = gols[:]
    cad['Total'] = sum(gols)
    cadgeral.append(cad.copy())
    cad.clear()
    gols.clear()
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Cadastrar outro jogador(S/N)? ')).strip().lower()[0]
    if continuar in 'n':
        break
print(cadgeral)
print('-=' * 30)
print(f'{"Cód. "}{"Nome":<15}{"Gols":<15}{"Total"}')
print('--' * 20)
for i, d in enumerate(cadgeral):
    print(f'{i:>4} ', end = '')
    for v in d.values():
        print(f'{str(v):<15}', end='')
    print()
print('--' * 20)
while True:
    detalhe = int(input('Digite o cód. para visualizar os detalhes: (999 para parar) '))
    if detalhe == 999:
        break
    elif detalhe >= len(cadgeral):
        print(f'CÓDIGO {detalhe} É INVÁLIDO')
    else:
        print(f'Levantamento do Jogador {cadgeral[detalhe]["Nome"]}')
        for j, g in enumerate(cadgeral[detalhe]['Gols']):
            print(f'No jogo {j + 1} fez {g} gols.')
print('<<<<<<FIM DO PROGRAMA>>>>>>')
