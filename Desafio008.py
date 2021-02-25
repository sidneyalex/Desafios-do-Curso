#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Valor em metros: '))
km = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('O valor informado de {}m corresponde a:'.format(m))
print('{}km'.format(km))
print('{}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
