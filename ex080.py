list = []

for c in range(0, 5):
    value = int(input('Digite um valor: '))
    if c == 0 or value > list[-1]:
        list.append(value)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(list):
            if value <= list[pos]:
                list.insert(pos, value)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {list}')