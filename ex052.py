number = int(input('Digite um número: '))
tot_divisivel = 0
for c in range(1, number + 1):
    if number % c == 0:
        c = f'\033[33m{c}\033[m'
        tot_divisivel += 1    
    print(f'\033[31m{c}\033[m', end=' ')
print()
print(f'O número {number} foi divisível {tot_divisivel} vezes')

if tot_divisivel == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')