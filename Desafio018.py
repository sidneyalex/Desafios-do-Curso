#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('\nPara o ângulo de {:.0f}° :\nSeno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}\n'.format(ang, seno, cosseno, tangente))
