#Crie um pgm que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionario se por acaso a CPTS for diferente de ZERO, o dicionario recebera tambem o ano de contratação e o salario. Calcule e acrescente além da idade com quantos anos a pessoa vai se aposentar(35 anos de contribuição)
from datetime import date
print(' === CADASTRO ===\n')
cad = {
    'nome': str(input('Nome: ')).strip(),
    'nascimento': int(input('Ano de nascimento: ')),
    'cpts': int(input('Carteira de Trabalho (0 se não tem): '))
}
hj = date.today().year
cad['idade'] = hj - cad['nascimento']
if cad['cpts'] != 0:
    cad['contratacao'] = int(input('Ano de Contratação: '))
    cad['salario'] = float(input('Salario: '))
    cad['aposentadoria'] = cad['contratacao'] + 35 - cad['nascimento']
print()
print('=-' * 30)
for k, v in cad.items():
    print(f'{k:<15}: {v}')
