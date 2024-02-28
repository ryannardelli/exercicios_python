dist = int(input('Qual é a distância da sua viagem? '))
if dist <= 200:
    preço_da_passagem = dist * 0.50
elif dist > 200:
    preço_da_passagem = dist * 0.45 
print(f'Você está prestes a começar uma viagem de R${dist:.1f}Km.')
print(f'E o preço da sua passagem será de R${preço_da_passagem:.2f}')