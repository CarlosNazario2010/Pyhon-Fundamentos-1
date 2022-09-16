print('===== ANALISADOR DE TRIANGULOS =====')

seg1 = float(input('DIGITE O PRIMEIRO SEGMENTO: '))
seg2 = float(input('DIGITE O SEGUNDO SEGMENTO: '))
seg3 = float(input('DIGITE O TERCEIRO SEGMENTO: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print('OS SEGMENTOS DIGITADOS SÃO CAPAZES DE FORMAR UM TRIANGULO')
else:
    print('OS SEGMENTOS DIGITADOS NÃO SÃO CAPAZES DE FORMAR UM TRIANGULO')