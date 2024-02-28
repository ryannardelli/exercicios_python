from random import randint
numeros = []
def sorteia(numeros):
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print('Sorteando 5 valores: ', end='')
    for value in numeros:
        print(value, end=' ')
    print('PRONTO!')
def somaPar(numeros):
    print(f'Sorteando os valores pares de {numeros}, temos', end=' ')
    totPar = 0
    for value in numeros:
        if value % 2 == 0:
            totPar += value
    print(f'{totPar}')
sorteia(numeros)
somaPar(numeros)