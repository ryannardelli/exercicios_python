soma = tot = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        tot += 1
print(f'A soma de todos os {tot} valores solicitados é {soma}')