print('===== SOMA DE TODOS OS NUMEROS IMPARES ENTRE 0 E 500 QUE SÃO MULTIPLOS DE 3 =====')

soma = 0

for c in range(1,501,2):

    if c % 3 == 0:
        soma = soma + c

print('A SOMA DE TODOS OS VALORES SOLICITADOS É: {}'.format(soma))