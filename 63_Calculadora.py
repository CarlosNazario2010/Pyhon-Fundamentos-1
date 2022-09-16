print(' ====== CALCULADORA ======')

while True:
    v1 = float(input('PRIMEIRO VALOR: '))
    v2 = float(input('SEGUNDO VALOR: '))
    operação = str(input('DIGITE A OPERAÇÃO:[+ - * /] '))

    if operação in '+':
        print('SOMA = {} '.format(v1 + v2))
    elif operação in '-':
        print('SUBTRACAO = {} '.format(v1 - v2))
    elif operação in '*':
        print('MULTIPLICACAO = {} '.format(v1 * v2))
    elif operação in '/':
        print('DIVISAO = {} '.format(v1 / v2))
    else:
        print('COMANDO INVALIDO')

    print('')
    continuar = str(input('FAZER NOVAMENTE [S/N] '))

    if continuar in 'Nn':
        print('PROGRAMA ENCERRADO.')
        break

