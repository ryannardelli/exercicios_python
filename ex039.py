import datetime
year_current = datetime.datetime.now().year
ano_nascimento = int(input('Ano de nascimento: '))
age = year_current - ano_nascimento
# print(year_current)
print(f'Quem nasceu em {ano_nascimento} tem {age} anos em {year_current}.')
if age < 18:
    ano_restante_para_alistamento = 18 - age
    ano_de_alistamento = year_current + ano_restante_para_alistamento
    print(f'Ainda faltam {ano_restante_para_alistamento} anos para o alistamento')
    print(f'Seu alistamento será em {ano_de_alistamento}')
elif age > 18:
    ano_que_ja_deveria_ter_alistado = age - 18
    ano_do_alistamento = year_current - ano_que_ja_deveria_ter_alistado
    print(f'Você já deveria ter se alistado há {ano_que_ja_deveria_ter_alistado} anos.')
    print(f'Seu alistamento foi em {ano_do_alistamento}.')
elif age == 18:
    print('Você tem que alistar IMEDIATAMENTE!')