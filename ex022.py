nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas é {nome.upper()}')
print(f'Seu nome em letras minúsculas é {nome.lower()}')
nome_com_espaços_removidos = nome.replace(' ', '')
print(f'Seu nome tem ao todo {len(nome_com_espaços_removidos)} letras')
primeiro_nome = nome.split()
print(f'Seu primeiro nome é {primeiro_nome[0]} e ele tem {len(primeiro_nome[0])} letras')