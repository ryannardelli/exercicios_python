while True:
    sexo = str(input('Informe seu sexo: [M/F] ').strip().upper())
    while sexo not in 'MmFf':
        sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper())
    if sexo in 'Mm':
        print(f'Sexo {sexo} registrado com sucesso')
        break
    
    if sexo in 'Ff':
        print(f'Sexo {sexo} registrado com sucesso')
        break
