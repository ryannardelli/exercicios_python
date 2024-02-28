person = {}
tot_gols = []
person['nome'] = str(input('Nome: '))
person['partidas'] = int(input(f'Quantas partidas {person["nome"]} jogou? '))
for c in range(person['partidas']):
    tot_gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    person['gols'] = tot_gols
person['total'] = sum(tot_gols)
print('-=' * 30)
print(person)
print('-=' * 30)
for key, value in person.items():
    print(f'O campo {key} tem o valor de {value}.')
print('-=' * 30)
print(f'O jogador {person["nome"]} jogou {person["partidas"]} partidas.')
for key, value in person.items():
    if key == 'partidas':
        for partida, gol in enumerate(tot_gols):
                print(f' -> Na partida, {partida + 1} fez {gol} gols.')
print(f'Foi um total de {sum(tot_gols)} gols.')