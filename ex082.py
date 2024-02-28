list_full = []
list_par = []
list_impar = []
while True:
    list_full.append(int(input('Digite um número: ')))
    choice = str(input('Deseja continuar? [S/N] ').strip().upper())

    while choice not in 'SsNn':
        choice = str(input('Deseja continuar? [S/N] ').strip().upper()) 

    if choice in 'Nn':
        break

for number in list_full:
    if number % 2 == 0:
        list_par.append(number)
    else:
        list_impar.append(number)   

print(f'A lista completa é {list_full}')
print(f'A lista de pares é {list_par}')
print(f'A lista de ímpares é {list_impar}')