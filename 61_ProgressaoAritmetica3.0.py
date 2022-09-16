print(' ===== GERADOR DE PA =====')

num = int(input('DIGITE O PRIMEIRO TERMO: '))
razao = int(input('DIGITE A RAZAO: '))
cont = 0
termo = num
mais = 10
total = 0

while mais != 0:
    total += mais
 
    while cont < total:
        print(' {} -> '.format(termo), end='')
        termo += razao
        cont += 1
 
    print(' PAUSA ')

    mais = int(input('MAIS QUANTOS VALORES: '))

print('FORAM {} TERMOS MOSTRADOS'.format(cont))
print(' FIM ')