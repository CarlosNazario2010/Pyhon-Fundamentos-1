print('===== CALCULADORA DE VALOR DE VIAGEM - ATÉ 200 KM R$ 0.50 POR KM. ACIMA R$ 0.45 POR KM =====')

viagem = float(input('QUAL FOI A DISTÂNCIA PERCORRIDA EM KM: '))

if viagem < 200:
    print(('O PREÇO DE SUA VIAGEM FOI: R$ {:.2f}'.format(viagem*0.5)))
else:
    print('O PREÇO DE SUA VIAGEM FOI: R$ {:.2f}'.format(viagem*0.45))