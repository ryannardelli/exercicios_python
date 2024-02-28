from time import sleep
from random import randint
print('\033[43m-=\033[m' * 30)
print('\033[44mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m')
print('\033[43m-=\033[m' * 30)
number_computer = randint(0, 5)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if num != number_computer:
    print(f'\033[41mGANHEI! Eu pensei no número {number_computer} e não no {num}\033[m')
elif number_computer == num:
    print(f'\033[43mPARABÉNS! Você conseguiu me vencer!\033[m')