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

def resumo(value=0, aumento=0, reduçao=0):
    print('-' *35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'{"Preço analisado"}: \t{moeda(value)}')
    print(f'{"Dobro do preço"}: \t{dobro(value)}')
    print(f'{"Metade do preço"}: \t{metade(value):>8}')
    print(f'{aumento}% de aumento: \t{aumentar(value, aumento)}')
    print(f'{reduçao}% de redução: \t{diminuir(value, reduçao)}')
    print('-' * 35)