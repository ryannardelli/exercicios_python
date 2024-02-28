from math import sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
c = co ** 2 + ca ** 2
h = sqrt(c)
print(f'A hipotenusa vai medir {h:.2f}')