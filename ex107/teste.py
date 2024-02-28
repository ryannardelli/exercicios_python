from modulo_ex107 import moeda
price = float(input('Digite o preço: R$'))
print(f'A metade de {price} é {moeda.metade(price)}')
print(f'O dobro de {price} é {moeda.dobro(price)}')
print(f'Aumentando 10%, temos {moeda.aumentar(price, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(price, 13)}')