#Faça um pgm q tenha uma função chamada área(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.
def área(largura, comprimento):
    print(f'O terreno informado tem {largura * comprimento}m²\n')


print('\nCalculo de Terrenos\n')
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
