def analisa_cidade_nascimento(cidade_nascimento):
    analisa_cidade = cidade_nascimento.split()
    if analisa_cidade[0] in 'santo':
        return True
    else:
        return False
cidade_nascimento = str(input('Em que cidade você nasceu? ').lower())
print(analisa_cidade_nascimento(cidade_nascimento))