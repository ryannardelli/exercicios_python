tot = cont_numeros_pares = 0
for c in range(0, 6):
    number = int(input(f'Digite o {c + 1}º valor: '))
    if number % 2 == 0:
        tot += number
        cont_numeros_pares += 1
print(f'Você informou {cont_numeros_pares} número(s) PARES e a soma foi {tot}')