def metade(value=0, format=True):
    res = value / 2
    if format == True:
        return f'R${res:.2f}'.replace('.', ',')
    else:
        return res

def dobro(value=0, format=True):
    res = value * 2
    if format == True:
        return f'R${res:.2f}'.replace('.', ',')
    else:
        return res

def aumentar(value=0, taxa=0, format=True):
    res = value + (value * taxa / 100)
    if format == True:
        return f'R${res:.2f}'.replace('.', ',')
    else:
        return res

def diminuir(value=0, taxa=0, format=True):
    res = value - (value * taxa / 100)
    if format == True:
        return f'R${res:.2f}'.replace('.', ',')
    else:
        return res

def moeda(value=0, moeda='R$'):
    return f'{moeda}{value:>.2f}'.replace('.', ',') 