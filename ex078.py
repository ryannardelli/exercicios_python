import sys
values = []
bigger = 0
smaller = sys.maxsize
pos_smaller = 0
pos_bigger = 0

for c in range(0, 5):
    values.append(int(input(f'Digite um valor para a Posição {c}: ')))

for pos, value in enumerate(values):
    if value > bigger:
        bigger = value
        pos_bigger = [pos]
    elif value == bigger:
        pos_bigger.append(pos)

    if value < smaller:
        smaller = value
        pos_smaller = [pos]
    elif value == smaller:
        pos_smaller.append(pos)

print(f'Você digitou os valores {values}')
print(f'O maior valor digitado foi {bigger} nas posições', *pos_bigger, sep=' ...')
print(f'O menor valor digitado foi {smaller} nas posições', *pos_smaller, sep=' ...')