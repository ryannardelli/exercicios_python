from datetime import date
year_current = date.today().year
def voto(ano_nasc):
    age = year_current - ano_nasc
    if age >= 16 and age < 18 or age > 65:
        return print(f'Com {age} anos: VOTO OPCIONAL.')
    if age >= 18:
        return print(f'Com {age} anos: VOTO OBRIGATÓRIO.')
    if age < 18:
        return print(f'Com {age} anos: NÃO VOTA.')
print('-=' * 20)
ano_nasc = int(input('Em que ano você nasceu? '))
voto(ano_nasc)