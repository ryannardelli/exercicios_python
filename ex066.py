list = []
tot = 0
while True:
    value = int(input('Digite um valor (999 para parar): '))
    if value != 999:
        list.append(value)
        tot += 1
    else:
        print(f'A soma dos {tot} valores resultou em {sum(list)}!')
        break
