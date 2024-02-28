totMan = 0
tot_bigger_twenty_Woman = 0
age_bigger_Eighteen = 0

while True:
    print('-=' * 10)
    print('Cadastre uma pessoa'.upper())
    print('-=' * 10)

    age = int(input('Idade: ').strip())
    genere = str(input('Sexo [M/F]: ').strip().upper())

    while genere not in 'MmFf':
        genere = str(input('Dados inválidos. Por favor, informe o seu sexo: [M/F]: ').strip().upper())
    
    choice = str(input('Quer continuar? [S/N] ').strip().upper())

    while choice not in 'NnSs':
        choice = str(input('Resposta inválida. Quer continuar? [S/N] '))

    if age > 18:
        age_bigger_Eighteen += 1
    
    if genere in 'Mm':
        totMan += 1

    if genere in 'Ff' and age < 20:
        tot_bigger_twenty_Woman += 1
    
    if choice in 'Nn':
        print('fim do programa'.upper())
        print(f'Total de pessoas com mais de 18 anos: {age_bigger_Eighteen}')
        print(f'Ao todo temos {totMan} homens cadastrados')
        print(f'E temos {tot_bigger_twenty_Woman} mulheres com menos de 20 anos')
        break