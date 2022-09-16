print('===== MOSTRE A SOMA DOS NÚMEROS PARES EM UMA SEQUÊNCIA DE SEIS NÚMEROS')

c = int(0)
soma = int(0)

for c in range(1,7):
    num = int(input('DIGITE SEU {}° NÚMERO: '.format(c)))

    if num % 2 == 0:
        soma = soma + num

print('A SOMA DOS NÚMEROS PARES DIGITADOS É: {}'.format(soma))
