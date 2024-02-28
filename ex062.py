print('Gerador de PA')
print('-=' * 10)
firstTerm = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

def PA(firstTerm, r):
    term = firstTerm
    tot = 0
    c = 1
    while c <= 10:
        print('{} ->'.format(term), end = ' ')
        term += r
        c += 1
        tot += 1
    print('PAUSA')
    
    while True:
        rest_term = int(input('Quantos termos você quer mostrar a mais? '))
        c = 1
        if rest_term == 0:
            print('Progressão finalizada com {} termos mostrados.'.format(tot))
            return
        else:
            while c <= rest_term:
                print('{} ->'.format(term), end = ' ')
                term += r
                c += 1
                tot += 1
            print('PAUSA')      
PA(firstTerm, r)