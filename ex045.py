from time import sleep
from random import randint
gera_jogada_computer = randint(0, 2)
jogada_player = jogada_computer = ''
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogada = int(input('Qual é a sua jogada? '))
while jogada not in [0, 1, 2]:
    jogada = int(input('Opção inválida. Por favor, insira uma opção válida: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-=' * 15)
if jogada == 0:
    jogada_player = 'Pedra'
elif jogada == 1:
    jogada_player = 'Papel'
elif jogada == 2:
    jogada_player = 'Tesoura'

if gera_jogada_computer == 0:
    jogada_computer = 'Pedra'
elif gera_jogada_computer == 1:
    jogada_computer = 'Papel'
elif gera_jogada_computer == 2:
    jogada_computer = 'Tesoura'

print(f'Computador jogou {jogada_computer}')
print(f'Jogador jogou {jogada_player}')

print('-=' * 15)

if jogada_player == 'Pedra' and jogada_computer == 'Tesoura':
    print('JOGADOR VENCE')
elif jogada_player == 'Tesoura' and jogada_computer == 'Papel':
    print('JOGADOR VENCE')
elif jogada_player == 'Papel'and jogada_computer == 'Pedra':
    print('JOGADOR VENCE')

if jogada_computer == 'Pedra' and jogada_player == 'Tesoura':
    print('COMPUTADOR VENCE')
elif jogada_computer == 'Tesoura' and jogada_player == 'Papel':
    print('COMPUTADOR VENCE')
elif jogada_computer == 'Papel'and jogada_player == 'Pedra':
    print('COMPUTADOR VENCE')

if gera_jogada_computer == jogada:
    print('EMPATE')