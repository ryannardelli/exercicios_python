list_full = [[], []]
for c in range(1, 8):
    number = int(input(f'Digite o {c}º valor: '))
    if number % 2 == 0:
        list_full[0].append(number)
    else:
        list_full[1].append(number)

print('-=' * 30)
list_full[0].sort()
print('Os valores pares digitados foram:', list_full[0])
list_full[1].sort()
print('Os valores ímpares digitados foram:', list_full[1])