list = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00,
        'Transferidor', 4.20, 'Compasso', 9.99,
        'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-=' * 20)
print(' ' * 10,'LISTAGEM DE PREÇOS', ' ' * 10)
print('-=' * 20)

for i in range(0, len(list), 2):
    print(list[i], '.' * 20, 'R${:.2f}'.format(list[i + 1]))
print('-=' * 20)