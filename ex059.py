from time import sleep
maior = 0
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
while True:
    sleep(0.5)
    print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa""")
    option = int(input('Qual é a sua opção? '))
    if option not in [1, 2, 3, 4, 5]:
        print('Opção inválida. Tente novamente')
        print('-=' * 15)
    else:
        if option == 1:
            print(f'A soma entre {v1} + {v2} é {v1 + v2}')
            print('-=' * 15)
        elif option == 2:
            print(f'O resultado de {v1} x {v2} é {v1 * v2}')
            print('-=' * 15) 
        elif option == 3:
            if v1 > v2:
                maior = v1
            else:
                maior = v2
            print(f'Entre {v1} e {v2} o maior valor é {maior}')
            print('-=' * 15)
        elif option == 4:
            print('Informe os números novamente:')
            v1 = int(input('Primeiro valor: '))
            v2 = int(input('Primeiro valor: '))
        else:
            print('Finalizando...')
            sleep(0.5)
            print('-=' * 15)
            print('Fim do programa! Volte sempre!')
            break