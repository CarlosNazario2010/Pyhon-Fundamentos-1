print('==== ALUGUEL DE CARROS ===== R$ 60,00 POR DIA E R$ O,15 POR KM RODADO')

km = float(input('QUANTOS KM FORAM RODADOS COM O CARRO: '))
dias = int(input('O CARRO FOI ALUGADO POR QUANTOS DIAS: '))

valorD = dias*60
valorK = km*0.15
valorT = valorD + valorK

print('O VALOR TOTAL A SE PAGAR POR {} DIAS E POR {:.2f} KM É DE {:.2f}'. format(dias,km,valorT))