#Crie um pgm que leia a vel de um carro.
#Se ele ultrapassar 80Km/h. mostra uma mensagem dizendo que ele foi multado.
#A multa vai custar  R$7,00 reais para cada Km acima do limite.
vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    print('Você foi multado por ultrapassar 80Km/h.')
    print('\nForam exedidos {}Km\h da velocidade permitida, pague R${},00'.format(vel - 80, (vel - 80) * 7))
else:
    print('Ok, dentro do esperado. Continue a boa direção.')
