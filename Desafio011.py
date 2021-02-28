#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
tamanho = altura * largura
print('O tamanho total da parede é de {}m² e você precisa de {:.1f} litros de tinta para pinta-la.'.format(tamanho, tamanho/2))
