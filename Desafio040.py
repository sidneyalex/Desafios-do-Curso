#Crie um pgm q leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#média abaixo de 5.0: Reprovado
#media entre 5.0 e 6.9: Recuperação
#média 7.0 ou superior: Aprovado
n1 = float(input('1ª NOTA: '))
n2 = float(input('2ª NOTA: '))
notafinal = (n1 + n2) / 2
if notafinal < 5:
    print('Sua nota Final é {}, REPROVADO.'.format(notafinal))
elif notafinal >= 5 and notafinal <= 6.9:
    print('Sua nota Final é {}, RECUPERAÇÃO.'.format(notafinal))
else:
    print('Sua nota Final é {}, APROVADO.'.format(notafinal))
