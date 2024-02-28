from random import randint
sorteia = randint(0, 4)   
ordem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto']
alunos = []
for c in range(0, 4):
    alunos.append(str(input(f'{ordem[c]} aluno: ')))
print(f'O aluno escolhido foi {alunos[sorteia]}')