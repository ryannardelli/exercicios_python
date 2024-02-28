import sys
maior_peso = 0
menor_peso = sys.maxsize
for c in range(1, 6):
    peso = float(input(f'Peso da {c}º pessoa: '))
    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso
print(f'O maior peso lido foi de {maior_peso}Kg')
print(f'O menor peso lido foi de {menor_peso}Kg')