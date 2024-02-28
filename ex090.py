person = {}
person['name'] = str(input('Nome: '))
person['media'] = float(input(f'Média de {person["name"]}: '))
print(f'Nome é igual a {person["name"]}')
print(f'Média é igual a {person["media"]}')
for key, value in person.items():
    if key == 'media':
        media = value    
        if media >= 7:
            print('Situação é igual a Aprovado')
        else:
            print('Situação é igual a Reprovado')