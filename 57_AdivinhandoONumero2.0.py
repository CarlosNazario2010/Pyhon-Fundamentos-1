from random import randint

print('===== VOU PENSAR EM UM NÚMERO DE 0 A 10. TENTE ADIVINHAR =====')

computador = randint(1,10)
jogador = 0
c = 0

while jogador !=  computador:
    jogador = int(input('DIGITE SEU PALPITE: '))
    c += 1

    if jogador > computador:
        print('MENOS')

    if jogador < computador:
        print('MAIS')

print('PENSEI NO NUMERO {}. VOCÊ VENCEU COM {} TENTATIVAS'.format(computador, c))

