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

def linha (tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leia_int('\033[32mSua Opção: \033[m')
    return opc