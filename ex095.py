person = {}
list_jogadores = []
print('-=' * 15)
while True:
    person['nome'] = str(input('Nome do Jogador: '))
    person['partidas'] = int(input(f'Quantas partidas {person["nome"]} jogou? '))
    tot_gols = []
    for c in range(0, person['partidas']):
        tot_gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    person['gols'] = tot_gols
    list_jogadores.append(person.copy())
    choice = str(input('Quer continuar? [S/N] ').strip().upper())
    print('-=' * 18)
    while choice not in 'SsNn':
        choice = str(input('Quer continuar? [S/N] ').strip().upper())
    if choice in 'Nn':
        break
print(f'{"cod":<4}{"nome":>5}{"gols":>7}{"total":>15}')
print('-=' * 18)
for c in range(0, len(list_jogadores)):
    tot_gols = sum(list_jogadores[c]['gols'])
    print(f'{c:<4}{list_jogadores[c]["nome"]:<8}{str(list_jogadores[c]["gols"]):<15}{tot_gols:>3}')
print('-=' * 18)
while True:
    dados = int(input('Mostrar dados de que jogador? '))
    if dados == 999:
        break
    try:
        list_jogadores[dados]
    except:
        print(f'ERRO! Não existe jogador com código {dados}! Tente novamente')
        print('-=' * 18)
    else:
        print(f'LEVANTAMENTO DO JOGADOR {list_jogadores[dados]["nome"]}:')
        for key, value in person.items():
            if key == 'partidas':
                for partida, gol in enumerate(list_jogadores[dados]['gols']):
                    print(f' -> No jogo {partida + 1} fez {gol} gols.')
                print('-=' * 18)
print('<< VOLTE SEMPRE >>')