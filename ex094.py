person = {}
list_person = []
tot_idades = media_idades = 0
while True:
    person['nome'] = str(input('Nome: '))
    person['sexo'] = str(input('Sexo: '))
    person['idade'] = int(input('Idade: '))
    list_person.append(person.copy())
    choice = str(input('Quer continuar? [S/N] ').strip().upper())
    while choice not in 'SsNn':
        choice = str(input('Quer continuar? [S/N] ').strip().upper())
    if choice in 'Nn':
        break
print('-='* 30)
print(f'O grupo tem {len(list_person)} pessoas.')
for c in range(0, len(list_person)):
    tot_idades += list_person[c]['idade']
    media_idades = tot_idades / len(list_person)
print(f'A média de idade é igual a {media_idades:.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for c in range(0, len(list_person)):
    if list_person[c]['sexo'] in 'Ff':
        print(list_person[c]['nome'], end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
for c in range(0, len(list_person)):
    if list_person[c]['idade'] > media_idades:
        person = list_person[c]
        for key, value in person.items():
            print(f'{key} = {value}; ', end='')
        print()
print('<< ENCERRADO >>')