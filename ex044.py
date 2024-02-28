print('=' * 10, 'LOJAS GUANABARA', '=' * 10)
price = float(input('Preço das compras: R$'))
while True:
    print("""[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
    option = int(input('Qual a sua opção? '))

    while option not in [1, 2, 3, 4]:
        option = int(input('Por favor, insira uma opção válida: '))

    if option == 1:
        desc = (price * 10) / 100
        new_price = price - desc
        print(f'Sua compra de R${price:.2f} vai custar R${new_price:.2f} no final.')
        break
    elif option == 2:
        desc = (price * 5) / 100
        new_price = price - desc
        print(f'Sua compra de R${price:.2f} vai custar R${new_price:.2f} no final.')
        break
    elif option == 3:
        price_dividido = price / 2
        print(f'Sua compra será parcelada em 2x de R${price_dividido:.2f} SEM JUROS.')
        break
    elif option == 4:
        parcelas = int(input('Quantas parcelas? '))
        juros = (price * 20) / 100
        new_price = price + juros
        print(f'Sua compra será parcelada em {parcelas}x de R${new_price:.2f} COM JUROS')
        print(f'Sua compra de R${price:.2f} vai custar R${new_price:.2f} no final.')
        break