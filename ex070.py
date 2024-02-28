print('-=' * 10)
print('LOJA SUPER BARATÃO')
print('-=' * 10)

import sys

bigger = 0
bigger_price = 0
smaller_price = sys.maxsize
tot_below_thousand = 0
listPrices = []
name_product_bigger = ''
name_product_smaller = ''

while True:
    product = str(input('Nome do Produto: '))
    price = int(input('Preço R$'))
    listPrices.append(price)

    if price > bigger_price:
        bigger_price = price
        name_product_price_bigger = product

    if price < smaller_price:
        smaller_price = price
        name_product_price_smaller = product

    if price > 1000:
        tot_below_thousand += 1

    choice = str(input('Quer continuar? [S/N] ').strip().upper())

    while choice not in 'SsNn':
        choice = str(input('Quer continuar? [S/N] ').strip().upper())

    if choice in 'Nn':
        print(f'O total da compra foi R${sum(listPrices)}')
        print(f'Temos {tot_below_thousand} produtos custando mais de R$1000') 
        print(f'O produto mais caro foi {name_product_price_bigger} que custa R${bigger_price}')
        print(f'O produto mais barato foi {name_product_price_smaller} que custa R${smaller_price}')
        break