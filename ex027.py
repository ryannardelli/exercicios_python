nome_completo = str(input('Digite seu nome completo: '))
nome_completo_separado = nome_completo.split()
primeiro_nome = nome_completo_separado[0]
ultimo_nome = nome_completo_separado[-1]
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')