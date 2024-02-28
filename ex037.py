number = int(input('Digite um número inteiro: '))
while True:
    print('Escolha uma das bases para conversão')
    print("""[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
    
    option = int(input('Sua opção: '))
    while option not in [1, 2, 3]:
        option = int(input('Opção inválida. Tente novamente: '))
    if option == 1:
        print(f'{number} convertido para BINÁRIO é igual a {bin(number)[2:]}')
        break
    elif option == 2:
        print(f'{number} convertido para OCTAL é igual a {oct(number)[2:]}')
        break
    elif option == 3:
        print(f'{number} convertido para HEXADECIMAL é igual a {hex(number)[2:]}')
        break