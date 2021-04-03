#Crie um pgm q tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados de forma tabular.
conteudo = ('Mouse', 40, 'Teclado', 80, 'Caixas de som', 50, 'Monitor', 700, 'Notebook', 2500)
print('='*30)
print(f'{"LOJINHA DE INFORMATICA":^30}')
print('='*30)
for c in range(0, len(conteudo)):
    if c % 2 == 0:
        print(f'{conteudo[c]:.<20}', end='')
    else:
        print(f'R${conteudo[c]:>8.2f}')
print('.'*30)
