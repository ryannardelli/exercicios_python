number = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for c in range(1, 11):
    print(f'{number} x {c} = {number * c}')
print('-' * 12)