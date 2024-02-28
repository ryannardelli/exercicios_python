list = []
tot = 0
while True:
    try:
        number = int(input('Digite um número: '))
        list.append(number)
        tot += 1
        medium = sum(list) / tot
    except:
        print('O valor inserido não é válido. Tente novamente.')
    else:
        response = str(input('Deseja continuar? [S/N] ').upper().strip())

        if response not in 'SsNn':
            raise Exception('Desculpe, a resposta precisa ser [S/N].')
        
        if response in 'Ss':
            continue
        else:
            print('Você digitou {} número(s) e a média foi {:.2f}.'.format(tot, medium))
            print('O maior valor foi {} e o menor foi {}.'.format(max(list), min(list)))
            break