def ficha(nome='', gols=0):
    try:
        gols = int(gols)
    except:
        gols = 0
    if nome == '':
        nome = '<desconhecido>'
    return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
print('-=' * 30)
nome = str(input('Nome do Jogador: '))
gols = input('Número de Gols: ')
ficha(nome, gols)