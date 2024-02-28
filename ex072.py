cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
     'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
     'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')


while True:
    number = int(input('Digite um número entre 0 e 20: '))

    while number < 0 or number > 20:
        number = int(input('Tente novamente. Digite um número entre 0 e 20: '))

    print(f'Você digitou o número {cont[number]}')

    choice = str(input('Deseja continuar? [S/N] ').strip().upper()) 

    while choice not in 'NnSs':
        choice = str(input('Deseja continuar? [S/N] ').strip().upper())

    if choice in 'Nn':
        print('Programa finalizado.')
        break
