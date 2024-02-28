from datetime import datetime
ano_atual = datetime.now().year
tot_idade_acima_de_18 = tot_idade_abaixo_de_18 = 0
for c in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    age = ano_atual - ano_nascimento
    if age >= 18:
        tot_idade_acima_de_18 += 1
    else:
        tot_idade_abaixo_de_18 += 1
print(f'Ao todo tivemos {tot_idade_acima_de_18} pessoas maiores de idade')
print(f'E também tivemos {tot_idade_abaixo_de_18} pessoas menores de idade')