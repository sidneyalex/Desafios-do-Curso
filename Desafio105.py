#Faça um pgm q tenha uma função notas() q pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação(Opcional)
# Adicione tambem as docstrings da função
def notas(*n, sit=False):
    """
    -> Recebe e analisa notas de varios alunos
    :param n: Notas dos alunos(uma ou mais)
    :param sit: (opcional) adiciona a situacao com base na media geral
    :return: dicionario com os valores Total, Maior, Menor, Media e Situacao(opcional)
    """
    resultado = {'Total': len(n)}
    resultado['Maior'] = max(n)
    resultado['Menor'] = min(n)
    resultado['Media'] = sum(n) / len(n)
    if sit:
        if resultado['Media'] <= 5:
            resultado['Situacao'] = 'Ruim'
        elif resultado['Media'] <= 7:
            resultado['Situacao'] = 'Razoável'
        else:
            resultado['Situacao'] = 'Boa'
    return resultado


resp = notas(5.5, 10, 4.5, 8.5, sit=True)
print(resp)
help(notas)