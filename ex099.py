from time import sleep
def maior(*num):
    maior = 0
    total = len(num)
    print('-=' * 20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        if valor > maior:
            maior = valor
    print(f'Foram informados {total} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    sleep(1)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()