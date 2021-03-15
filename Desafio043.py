#Desenvolva uma logica q leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5:Abaixo do Peso
#Entre 18.5 e 25:Peso ideal
#25 até 30:Sobrepeso
#30 até 40:Obesidade
#acima de 40:Obesidade Morbida
altura = float(input('Qual sua altura: (m) '))
peso = float(input('Qual seu peso: (Kg) '))
IMC = peso / (altura ** 2)
print('Seu IMC é {:.1f}, você tem '.format(IMC), end='')
if IMC < 18.5:
    print('ABAIXO DO PESO')
elif IMC < 25:
    print('PESO IDEAL')
elif IMC < 30:
    print('SOBREPESO')
elif IMC < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
