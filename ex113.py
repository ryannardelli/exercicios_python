def leia_int(value):
    while True:
        try:
            value = int(input(value))
        except ValueError:
            print('\033[0;31mERRO: Por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            value = 0
            return value
        else:
            return value
def leia_float(value):
    while True:
        try:
            value = float(input(value))
        except ValueError:
            print('\033[0;31mERRO: Por favor, digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            value = 0
            return value
        else:
            return value
numero_inteiro = leia_int('Digite um Inteiro: ')
numero_real = leia_float('Digite um Real: ')
print(f'O valor inteiro digitado foi {numero_inteiro} e o real foi {numero_real}')