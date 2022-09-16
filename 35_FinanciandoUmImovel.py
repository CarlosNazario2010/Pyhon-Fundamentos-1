print('===== FINANCIAMENTO HABITACIONAL =====')

casa = float(input('QUAL É O VALOR DO IMÓVEL: R$ '))
salario = float(input('QUAL O SALÁRIO DO TOMADOR: R$ '))
tempo = float(input('EM QUANTOS ANOS PRETENDE FINANCIAR: '))

prestacao = casa/(tempo*12)

if prestacao < (salario*0.3):
    print('FINANCIAMENTO APROVADO COM PRESTAÇÃO DE R$ {:.2f}'.format(prestacao))
else:
    print('FINANCIAMENTO NEGADO. VALOR DE PRESTAÇÃO DE R$ {:.2f} MAIOR QUE 30% DO SALARIO'.format(prestacao))
