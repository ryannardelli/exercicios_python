def metade(value=0):
    res = value / 2
    return res

def dobro(value=0):
    res = value * 2
    return res

def aumentar(value=0, taxa=0):
    res = value + (value * taxa / 100)
    return res

def diminuir(value=0, taxa=0):
    res = value - (value * taxa / 100)
    return res

def moeda(value=0, moeda='R$'):
    return f'{moeda}{value:>.2f}'.replace('.', ',')