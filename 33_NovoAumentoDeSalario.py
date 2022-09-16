salario = float(input('QUAL É O SALÁRIO DO FUNCIONÁRIO: R$ '))

if salario < 1250:
    print('O NOVO SALÁRIO COM 15% DE AUMENTO É {:.2f}'.format(salario*1.15))
else:
    print('O NOVO SALÁRIO COM 10% DE AUMENTO É {:.2f}'.format(salario * 1.10))