while True:
    value = int(input('Quer ver a tabuada de qual valor? '))
    if value >= 0:
        c = 0
        for c in range(1, 11):
            print(f'{value} x {c} = {value * c}')
    else:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break