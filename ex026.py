frase = str(input('Digite uma frase: ').upper().strip())
quant_letra_a = frase.count('A')
pos_primeira_letra_a = frase.find('A') + 1
pos_ultima_letra_a = frase.rfind('A') + 1
print(f'A letra A aparece {quant_letra_a} vezes na frase.')
print(f'A primeira letra A apareceu na posição {pos_primeira_letra_a}')
print(f'A última letra A apareceu na posição {pos_ultima_letra_a}')