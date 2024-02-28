n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
values = (n1, n2, n3, n4)

def num_par(num):
     return num % 2 == 0

tot_par = tuple(filter(num_par, values))
print(f'Você digitou os valores {values}')
print(f'O valor 9 apareceu {values.count(9)} vezes')

try:
    values.index(3)
except:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {values.index(3) + 1}º posição')

print('Os valores pares digitados foram:', *tot_par, sep=' ')


