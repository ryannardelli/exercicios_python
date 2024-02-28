def area(larg, alt):
    area = larg * alt
    return area
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area(largura, altura)}m².')
tinta = area(largura, altura) / 2
print(f'Para pintar essa parede, você precisará de {tinta}L de tinta.')