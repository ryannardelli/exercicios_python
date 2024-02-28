list_alunos = [[], []]
notes = []
while True:
    list_alunos[0].append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    medium = (n1 + n2) / 2
    medium = '{:.1f}'.format(medium)
    notes = [n1, n2, medium]
    list_alunos[1].append(notes[:])
    choice = str(input('Quer continuar? [S/N] ').strip().upper())
    while choice not in 'SsNn':
        choice = str(input('Quer continuar? [S/N] ').strip().upper()) 
    if choice in 'Nn':
        break
print('-=' * 30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for pos, name in enumerate(list_alunos[0]):
    print(f'{pos:<4}{name:<10}{list_alunos[1][pos].pop():>8}')
print('-' * 26)
while True:
    response = int(input('Mostrar nota de qual aluno? (999 para interromper): '))
    if response == 999:
        break
    print(f'Notas de {list_alunos[0][response]} são {list_alunos[1][response]}')
    print('-=' * 20)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')