def analisa_nome(nome_completo):
    if nome_completo.count('silva') >= 1:
        return True
    else:
        return False
nome_completo = str(input('Qual é seu nome completo? ').lower())
print(f'Seu nome tem Silva? {analisa_nome(nome_completo)}')