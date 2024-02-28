print('-=' * 5)
print('BANCO CEV')
print('-=' * 5)
value = int(input('Qual valor você quer sacar? R$'))
tot = value
bank_notes = 100
tot_bank_notes = 0
while True:
    if tot >= bank_notes:
        tot -= bank_notes
        tot_bank_notes += 1
    else:
        if tot_bank_notes > 0:
            print(f'Total de {tot_bank_notes} cédulas de R${bank_notes}')
    
        if bank_notes == 100:
            bank_notes = 50
        elif bank_notes == 50:
            bank_notes = 20
        elif bank_notes == 20:
            bank_notes = 10
        elif bank_notes == 10:
            bank_notes = 5
        elif bank_notes == 5:
            bank_notes = 2
        elif bank_notes == 2:
            bank_notes = 1
        tot_bank_notes = 0

        if tot == 0:
            break
print('Volte sempre ao BANCO CEV. Tenha um bom dia!')