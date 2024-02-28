def contador():
    print('-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1, 11):
        print(c, end=' ')
    print('FIM!')
    print('-=' * 20)
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10, 0, -2):
        print(c, end=' ')
    print('FIM!')
    print('-=' * 20)
    print('Agora é a sua vez de personalizar a Contagem!')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    if inicio < fim:
        if passo <= 0:
            passo = 1
        print('-=' * 20)
        print(f'Contagem de {inicio} até {fim} de {passo} e {passo}')
        for c in range(inicio, fim + 1, passo):
            print(c, end=' ')
    else:
        if passo <= 0:
            passo = 1
        print('-=' * 20)
        print(f'Contagem de {inicio} até {fim} de {passo} e {passo}')
        for c in range(inicio, fim - 1, - passo):
            print(c, end=' ')
    print('FIM!')
contador()