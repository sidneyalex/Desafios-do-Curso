#Crie um pgm q gerencie o aproveitamento de um jogador de futebol. O pgm vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionario, incluindo o total de gols feitos durante o campeonato
cad = {'Nome': str(input('Nome do jogador: '))}
partidas = int(input(f'Quantas partidas {cad["Nome"]} jogou? '))
gols = list()
for g in range(0, partidas):
    gols.append(int(input(f'Gols na partida {g + 1}: ')))
cad['Gols'] = gols[:]
cad['Total'] = sum(gols)
print('-=' * 30)
print(cad)
print('-=' * 30)
for k, v in cad.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 30)
print(f'O jogador {cad["Nome"]} jogou {len(cad["Gols"])} partidas.')
for i, g in enumerate(cad['Gols']):
    print(f' => Partida {i+1} - {g} gols.')
print(f'Foi um total de {cad["Total"]} gols.')
