
def addNumbers():
    list = []
    tot = 0
    while True:
        number = int(input('Digite um número (999 para parar): '))
        if number != 999:
            list.append(number)
            tot += 1
        else:
            print('Você digitou {} números e a soma entre eles foi {}.'.format(tot, sum(list)))
            return
addNumbers()