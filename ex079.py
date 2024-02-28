values = []

def analyze(el, list):
    if el in list:
        print('Valor duplicado! Não vou adicionar...')
    else:
        list.append(el)
        print('Valor adicionado com sucesso...')

while True:
    value = int(input('Digite um valor: '))
    analyze(value, values)
    choice = str(input('Deseja continuar? [S/N] ').strip().upper())
    
    while choice not in 'SsNn':
        choice = str(input('Deseja continuar? [S/N] ').strip().upper())

    if choice in 'Nn':
        break
    
print('-=' * 20)
values.sort()
print(f'Você digitou os valores {values}')