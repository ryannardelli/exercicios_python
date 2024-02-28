from time import sleep
c = (
  '\033[m', # 0 - sem cores
  '\033[0;30;41m', # 1 - vermelho
  '\033[0;30;42m', # 2 - verde
  '\033[0;30;43m', # 3 - amarelo
  '\033[0;30;44m', # 4 - azul
  '\033[0;30;45m', # 5 - roxo
  '\033[7;30m'     # 6 - branco
)
def ajuda(comando):
  titulo(f'Acessando o manual do comando \'{comando}\'', 4)
  print(c[6], end='')
  help(comando)
  print(c[0], end='')
  sleep(2)

def titulo(msg, cor=0):
  tamanho = len(msg) + 4
  print(c[cor], end='')
  print('~' * tamanho)
  print(f'  {msg}')
  print('~' * tamanho)
  print(c[0], end='')
  sleep(1)
while True:
  titulo('SISTEMA DE AJUDA PYHELP', 2)
  response = str(input('Função ou Biblioteca > '))
  if response.upper() in 'FIM':
    break
  else:
    ajuda(response)
titulo('ATÉ LOGO!', 1)