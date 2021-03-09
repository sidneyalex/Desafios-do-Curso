#crie um pgm q pergunte a dist de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
viagem = int(input('Digite a distancia da viagem: Km'))
'''if viagem <= 200:
    print('O valor da passagem esta R${:.2f}, boa viagem'.format(viagem * 0.50))
else:
    print('Sua passagem teve R${:.2f} de desconto e sai por R${:.2f}. Boa viagem.'.format(viagem * 0.05, viagem * 0.45))'''
preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
