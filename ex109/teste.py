from modulo_ex109 import moeda
price = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(price)} é {moeda.metade(price, True)}')
print(f'O dobro de {moeda.moeda(price)} é {moeda.dobro(price, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(price, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(price, 13, True)}')