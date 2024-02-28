tot_idade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
tot_idade_mulheres_abaixo_de_20 = 0
for c in range(1, 5):
    print('-' * 5, f'{c}º Pessoa', '-' * 5)
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ').strip().upper())
    while sexo not in 'MmFF':
        sexo = str(input('Sexo: [M/F]: ').strip().upper())
    tot_idade += age
    media = tot_idade / 4
    if sexo in 'Mm':
        if age > idade_homem_mais_velho:
            idade_homem_mais_velho = age
            nome_homem_mais_velho = name
    if sexo in 'Ff':
        if age < 20:
            tot_idade_mulheres_abaixo_de_20 += 1
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho tem {idade_homem_mais_velho} anos e se chama {nome_homem_mais_velho}.')
print(f'Ao todos são {tot_idade_mulheres_abaixo_de_20} mulheres com menos de 20 anos.')