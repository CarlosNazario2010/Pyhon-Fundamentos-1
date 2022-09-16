from random import randint

computador = randint(0,5)

print('===== VOU PENSAR EM NÚMERO DE 0 A 5, TENTE ADIVINHAR =====')

num = int(input('EM QUE NÚMERO EU PENSEI: '))

if computador == num:
    print('PARABENS!!! VOCÊ GANHOU, EU PENSEI NO NUMERO {}'.format(computador))
else:
    print('VOCÊ PERDEU!!! EU PENSEI NO NÚMERO {}'.format(computador))

