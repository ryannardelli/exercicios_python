dias_alugado = int(input('Quantos dias alugados: '))
km_rodado = float(input('Quantos Km rodados: '))
total_a_pagar = (60 * dias_alugado) + (0.15 * km_rodado) 
print(f'O total a pagar é de R$ {total_a_pagar:.2f}')