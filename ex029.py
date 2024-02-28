vel = int(input('Qual é a velocidade atual do carro? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('\033[41mMULTADO! Você excedeu o limite permitido que é de 80Km/h\033[m')
    print(f'\033[41mVocê deve pagar uma multa de\033[m \033[43mR${multa:.2f}!\033[m')
print('\033[43mTenha um bom dia! Dirija com segurança!\033[m')