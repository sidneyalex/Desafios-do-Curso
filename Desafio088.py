#Faça um pgm q ajude um jogador da MEGA SENA a criar palpites. O pgm vai perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
mega = list()
jogo = list()
num = 0
print('-=' * 16)
print('GERADOR DE PALPITES DA MEGA SENA')
print('-=' * 16)
quant = int(input('\nQuantos palpites quer gerar? '))
for j in range(0, quant):
    for n in range(0, 6):
        while True:    
            num = randint(1, 60)
            if num not in jogo:
                jogo.append(num)
                break
    jogo.sort()
    mega.append(jogo[:])
    jogo.clear()
print()
for i, r in enumerate(mega):
    print(f'Jogo{i + 1}: {r}')
