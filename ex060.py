from math import factorial

number = int(input('Digite o número que você deseja saber o fatorial: '))
factorial = factorial(number)
c = number
print('Calculando !{} ='.format(number), end=' ')
while c > 0:
    print('{}'.format(c, factorial), end = ' ')
    print(' x ' if c > 1 else ' = {} '.format(factorial), end=' ') 
    c -= 1