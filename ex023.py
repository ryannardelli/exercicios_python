num = int(input('Informe um número: '))
numero_em_string = str(num)
print(f'Analisando o número {num}')
numero_em_string.split()
print(len(numero_em_string))

if len(numero_em_string) >= 4:
    milhar = numero_em_string[0]
else:
    milhar = 0

if len(numero_em_string) >= 2:
    dezena = numero_em_string[-2]
else:    
    dezena = 0

if len(numero_em_string) >= 3:
    centena = numero_em_string[-3]
else:
    centena = 0

unidade = numero_em_string[-1]

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')