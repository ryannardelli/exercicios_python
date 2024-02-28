def fatorial(number, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param number: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número number.
    """
    f = 1
    for c in range(number, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
help(fatorial)