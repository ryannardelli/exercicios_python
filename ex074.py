from random import randint

n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
values = (n1, n2, n3, n4, n5)
print('Os valores sorteados foram:', *values, sep=' ')
print(f'O maior valor é {max(values)}')
print(f'O menor valor é {min(values)}')