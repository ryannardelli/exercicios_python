from random import shuffle
ordem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto']
alunos = []
for c in range(0, 4):
    alunos.append(str(input(f'{ordem[c]} aluno: ')))
shuffle(alunos)
print(f'A ordem de apresentação será {alunos}')