persons = []
data = []
bigger = smaller = 0
while True:
    name = str(input('Nome: '))
    weight = float(input('Peso: '))
    data = [name, weight]
    persons.append(data[:])
    if len(persons) == 1:
        bigger = smaller = data[1]
    else:
        if data[1] > bigger:
            bigger = data[1]
        if data[1] < smaller:
            smaller = data[1]  
    choice = str(input('Quer continuar? [S/N] ').strip().upper())
    while choice not in 'SnNn':
        choice = str(input('Quer continuar? [S/N] ').strip().upper())  

    if choice in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo, você cadastrou {len(persons)} pessoas.')
print(f'O maior peso foi de {bigger}kg. Peso de ', end='')
for person in persons:
    if person[1] == bigger:
        print(f'[{person[0]}] ', end='')
print() 
print(f'O menor peso foi de {smaller}kg. Peso de ', end='')
for person in persons:
    if person[1] == smaller:
        print(f'[{person[0]}] ', end='')