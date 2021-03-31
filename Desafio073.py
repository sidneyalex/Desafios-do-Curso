#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#A)Apenas os 5 primeiros colocados.
#B)Os últimos 4 colocados da tabela.
#C)Uma lista com os times em ordem alfa
#D)Em que posição na tabela está o time da Chapecoense.
times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense',
    'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará',
    'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco',
    'Goiás', 'Coritiba', 'Botafogo')
print('-=' * 15)
print(f'Os 5 primeiros colocados foram: {times[:5]}')
print('-=' * 15)
print(f'Os 4 ultimos colocados foram: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alphabetica: {sorted(times)}')
print('-=' * 15)
print(f'Athletico-PR está na {times.index("Athletico-PR")+1}º posição')
