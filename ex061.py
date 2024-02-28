print('Gerador de PA')
print('-=' * 10)
firstTerm = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))


def PA(firstTerm, r):
    term = firstTerm
    c = 1
    while c <= 10:
        print('{} ->'.format(term), end=' ')
        term += r
        c += 1
    print('FIM')

PA(firstTerm, r)