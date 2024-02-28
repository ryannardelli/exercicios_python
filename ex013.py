salario = float(input('Qual é o salário do funcionário? R$ '))
aumento = (salario * 15) / 100
new_salario = salario + aumento
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${new_salario:.2f}')