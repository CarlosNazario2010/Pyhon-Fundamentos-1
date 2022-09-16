print(' ===== SEQUENCIA DE FIBONACCI =====')

quant = int(input('QUANTOS TERMOS DESEJA VER: '))

v1 = 0
v2 = 1

print(' {} -> {} -> '.format(v1, v2), end='')

c = 2
denovo = ''

while True:

    while c < quant:
        v3 = v1 + v2
        print(' {} -> '.format(v3), end='')
        v1 = v2
        v2 = v3
        c += 1

    denovo = str(input('\nCONTINUAR [S/N]: ').upper())

    if denovo == 'N':
        break

    quant = int(input('QUANTOS TERMOS DESEJA VER: '))
    quant += c

print('FIM')

