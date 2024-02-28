from random import randint
print('-=' * 13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 13)
valueComputer = randint(1, 10)
tries = 0
while True:
    value = int(input('Digite um valor: '))
    choice = str(input('Par ou Ímpar? [P/I] ').strip().upper())
    if choice not in 'PpIi':
        raise Exception('[Erro] Desculpe, a resposta precisa ser [P/I]')
    
    if choice in 'Ii' or choice in 'Pp':
        tot = value + valueComputer
        if tot % 2 >= 1:
            print(f'Você jogou {value} e o computador jogou {valueComputer}, Total de {tot} DEU ÍMPAR')
        else:
            print(f'Você jogou {value} e o computador jogou {valueComputer}, Total de {tot} DEU PAR')

        if choice in 'Pp' and tot % 2 == 0 or choice in 'Ii' and tot % 2 >= 1:
            print('Você GANHOU!')
            tries += 1
        else:
            print(f'GAME OVER! Você venceu {tries} veze(s).')
            break