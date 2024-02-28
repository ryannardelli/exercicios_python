teams = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense',
         'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro',
         'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG'
)

print('-=' * 20)
print('Lista de times do Brasileirão: ', teams)
print('-=' * 20)
print('Os 5 primeiros são', teams[0:5])
print('Os 4 últimos são', teams[-4:])
print('Times em ordem alfabética: ', sorted(teams))
print('-=' * 20)
print('O Corinthians está na {}º posição'.format(teams.index('Corinthians') + 1))