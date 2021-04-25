#Faça um pgm q tenha uma função chamada escreva(), que receba um texto qualquer como parãmetro e mostre uma msg com tamanho adaptável.
# Ex: escreva('Olá, Mundo!')
# Saida:
# ~~~~~~~~~~~~~
#  Olá, Mundo! 
# ~~~~~~~~~~~~~
def escreva(texto):
    print()
    print('~' * (len(texto) + 2))
    print(f' {texto} ')
    print('~' * (len(texto) + 2))


escreva('Sidney Silva')
escreva('Aprendendo Phyton')
escreva('Com o Guanabara')
