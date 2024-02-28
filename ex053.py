frase = str(input('Digite uma frase: ').upper()).replace(' ', '')
frase_invertida = frase[::-1]
print(f'O inverso de {frase} é {frase_invertida}')
if frase == frase_invertida:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')