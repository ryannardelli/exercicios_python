from datetime import date
ano_atual = date.today().year
person = {}
person['nome'] = str(input('Nome: '))
ano_nasc =  int(input('Ano de nascimento: '))
person['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
person['idade'] = ano_atual - ano_nasc
if person['ctps'] != 0:
    person['contratação'] = int(input('Ano de contratação: '))
    person['aposentadoria'] = (person['contratação'] + 35) - ano_nasc 
    person['salário'] = float(input('Salário: R$ '))
print('-=' * 30)
for key, value in person.items():
    print(f'{key} tem o valor {value}')