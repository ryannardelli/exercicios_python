from random import randint
number_computer = randint(0, 10)
tries = 0
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi? ')
while True:
    palpite = int(input('Qual seu palpite? '))
    if palpite < number_computer:
        print('Mais... tente mais uma vez.')
        tries += 1
    elif palpite > number_computer:
        print('Menos... tente mais uma vez.')
        tries += 1
    else:
        tries += 1
        print(f'Acertou com {tries} tentativa(s). Parabéns!')
        break