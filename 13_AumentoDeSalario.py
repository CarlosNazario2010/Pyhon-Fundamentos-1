s = float(input('QUAL O SALÁRIO DO FUNCIONÁRIO: R$ '))
a = float(input('QUAL O PERCENTUAL DE AUMENTO: '))

ns = s * (1+a/100)

print('O NOVO SALÁRIO DO FUNCIONÁRIO COM {:.2f}% DE AUMENTO É DE R$ {:.2F}'.format(a,ns))