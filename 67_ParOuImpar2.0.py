from random import randint
print(' ====== PAR OU IMPAR ======')

vitjog = 0
vitcomp = 0

while True:
    print('')
    jogar = str(input('DESEJA JOGAR [S/N]:'))
   
    if jogar in 'Nn':
        print('VOCE VENCEU {} E O COMPUTADOR VENCEU {}. FORAM JOGADAS {} PARTIDAS'.format(vitjog, vitcomp, vitjog +vitcomp))
        print('PROGRAMA ENCERRADO.')
        break
   
    num = int(input('NUMERO DO JOGADOR: '))
    computador = randint(1, 10)
    opcao = str(input('PAR OU IMPAR [P/I] '))
    soma = num + computador

    if soma % 2 == 0 and opcao in 'Pp':
        vitjog += 1
        print ('COMPUTADOR JOGOU {}, SOMA = {}, PAR!!!!, VOCE VENCEU!!!!'.format(computador, soma))
    elif soma % 2 == 0 and opcao in 'Ii':
        vitcomp += 1
        print ('COMPUTADOR JOGOU {}, SOMA = {}, PAR!!!!, VOCE PERDEU!!!!'.format(computador, soma))
    elif soma % 2 == 1 and opcao in 'Pp':
        vitcomp += 1
        print ('COMPUTADOR JOGOU {}, SOMA = {}, IMPAR!!!!, VOCE PERDEU!!!!'.format(computador, soma))
    elif soma % 2 == 1 and opcao in 'Ii':
        vitjog += 1
        print ('COMPUTADOR JOGOU {}, SOMA = {}, IMPAR!!!!, VOCE VENCEU!!!!'.format(computador, soma))
