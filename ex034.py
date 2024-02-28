salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    novo_salario = ((salario * 10) / 100) + salario
if salario <= 1250:
    novo_salario = ((salario * 15) / 100) + salario
print(f'Quem ganhava R${salario} passa a ganhar R${novo_salario:.2f} agora.')