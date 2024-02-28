n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media:.1f}')
if media < 5:
    print('O aluno está REPROVADO.')
elif media >= 5 and media < 6.9:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')