print('===== GERADOR DE PA =====')

num = int(input('DIGITE O PRIMEIRO TERMO: '))
razao = int(input('DIGITE A RAZAO: '))

#### UTILIZANDO O COMANDO WHILE

quant = 0
mais = 10
continuar = 's'

while continuar == 's':

    while quant < mais:
        print(' {} '.format(num), end='')
        num += razao
        quant += 1

    print(' PAUSA ')
    continuar = str(input('DESEJA CONTINUAR [S/N] ')).lower()

    if continuar != 's':
        break

    quant = int(input('MAIS QUANTOS TERMOS: '))
    quant -= mais
    quant *= -1

print('')
print(' PROGRAMA ENCERRADO ')





#### UTILIZANDO O COMANDO FOR

#quant = 0
#mais = 10
#continuar = 's'
#while continuar == 's':
#    quant += mais
#    for quant in range(0, quant):
#        print(' {} ->'.format(num), end='')
#        num += razao
#        quant += 1
#    print(' PAUSA ')
#    continuar = str(input('DESEJA CONTINUAR [S/N] ')).lower()
#    if continuar != 's':
#        break
#    quant = int(input('MAIS QUANTOS TERMOS: '))
#    quant -= mais
#print('')
#print(' PROGRAMA ENCERRADO ')
