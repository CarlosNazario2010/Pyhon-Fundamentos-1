print('===== RADAR DE VELOCIDADE DE TRÂNSITO =====')

velocidade = float(input('QUAL A VELOCIDADE DO VEÍCULO EM KM/H: '))
multa = float((velocidade - 80)*7)

if velocidade > 80:
    print('VOCÊ ULTRAPASSOU O LIMITE DE VELOCIDADE E FOI MULTADO EM R$ {:.2f}'.format(multa))
else:
    print('DIRIJA COM SEGURANÇA!!!')
