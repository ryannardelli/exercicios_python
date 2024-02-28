import datetime
year_current = datetime.datetime.now().year
ano_nasc = int(input('Ano de Nascimento: '))
age = year_current - ano_nasc
print(f'O alteta tem {age} anos.')
if age <= 9:
    print('Classificação: MIRIM')
elif age <= 14:
    print('Classificação: INFANTIL')
elif age <= 19:
    print('Classificação: JÚNIOR')
elif age <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')