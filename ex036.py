value_house = float(input('Valor da Casa: R$'))
salario_comprador = float(input('Salário do comprador: R$'))
anos_de_financiamento = int(input('Quantos anos de financiamento: '))
prestação = value_house / anos_de_financiamento
porcentagem_salarial = (30 / 100) * salario_comprador
prestação_mensal = value_house / (anos_de_financiamento * 12)
print(f'Para pagar uma casa de R${value_house:.2f}, em {anos_de_financiamento} anos, a prestação será de R${prestação_mensal:.2f}')
if prestação_mensal > porcentagem_salarial:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEBIDO!')