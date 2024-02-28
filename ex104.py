def leiaint(value):
    while True:
        try:
            value = int(input(value))
            return value
        except ValueError:
            print('\033[91mERRO! Digite um número inteiro válido.')
print('-=' * 20)
number = leiaint('\033[0mDigite um número: ')
print(f'Você acabou de digitar o número {number}')