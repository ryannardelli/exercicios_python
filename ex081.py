values = []
while True:
    values.append(int(input('Digite um valor: ')))
    choice = str(input('Deseja continuar? [S/N] ').strip().upper())

    while choice not in 'SsNn':
        choice = str(input('Deseja continuar? [S/N] ').strip().upper())

    if choice in 'Nn':
        break

print('-=' * 30)
print(f'Você digitou {len(values)} elementos.')
values.sort(reverse=True)
print(f'O valor em ordem decrescente são {values}')
if 5 in values:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')     