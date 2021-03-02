#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''1ª RESOLUÇÃO
import math
op = float(input('Digite o comprimento do cateto oposto: '))
ad = float(input('Digite o comprimento do cateto adjacente: '))
print(math.hypot(op, ad))'''

'''2ª RESOLUÇÃO
from math import hypot
catopo = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa é {:.2f} para os catetos {} e {}.'.format(hypot(catopo, catadj), catopo, catadj))'''

cat1 = float(input('Comprimento Cateto oposto: '))
cat2 = float(input('Comprimento Cateto adjacente: '))
hip = (cat1 ** 2 + cat2 ** 2)  ** (1/2)
print('Com os catetos {} e {} a hipotenusa vai medir {:.2f}.'.format(cat1, cat2, hip))
