price = float(input('Qual o preço do produto? R$ '))
desc = (price * 5) / 100
new_price = price - desc
print(f'O produto que custava R${price}, na promoção com desconto de 5% vai custar R${new_price:.2f}')