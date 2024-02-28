import sys
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
maior = 0
menor = sys.maxsize
if v1 > maior:
    maior = v1

if v2 > maior:
    maior = v2

if v3 > maior:
    maior = v3

if v1 < menor:
    menor = v1

if v2 < menor:
    menor = v2

if v3 < menor:
    menor = v3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')