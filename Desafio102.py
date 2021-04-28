#Crie um pgm q tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o numero a calcular e o outro chamado show, q será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do factorial.
def fatorial(num, show=False): 
    """
    -> Calculo de Fatorial
    :param num: Numero a ser calculado
    :param show: (opcional) mostra o calculo
    :return: fatorial de num
    """
    from math import factorial
    if show:
        for n in range(num, 0, -1):
            if n == 1:
                print(f'{n} = ', end='')
            else:
                print(f'{n} x ', end='')
    return factorial(num)


print(fatorial(5, True))
help(fatorial)