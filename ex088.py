from random import randint
from time import sleep
palpitations = []
def sorteia_numeros():
    numbers = []
    while len(numbers) < 6:
        new_number = randint(1, 60)
        if new_number not in numbers:
            numbers.append(new_number)
    return numbers
print('-=' * 20)
print(' ' * 10, 'JOGA NA MEGA SENA', ' ' * 10)
print('-=' * 20)
games = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(games):
    numbers = sorteia_numeros()
    palpitations.append(numbers)
print('-=' * 5, f'   SORTEANDO {games} JOGOS', ' ' * 5, '-=' * 5)
for index, game in enumerate(palpitations):
    print(f'Jogo {index + 1}: {game}')
    sleep(2)
print('-=' * 5, ' < BOA SORTE! > ', '-=' * 6)