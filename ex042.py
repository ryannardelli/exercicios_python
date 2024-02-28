s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

def analisa_triangulo(a, b, c):
    if a == b == c:
        return 'EQUILÁTERO!'
    elif a == b or a == c or b == c:
        return 'ISÓSCELES!'
    else:
        return 'ESCALENO!'
    
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print(f'Os segmentos acima PODEM FORMAR um triângulo {analisa_triangulo(s1, s2, s3)}')
else:
    print('O segmentos acima NÃO PODEM FORMAR triângulo!')