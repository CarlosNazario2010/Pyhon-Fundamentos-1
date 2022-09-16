from random import randint
from time import sleep

print('===== JOGO DE PEDRA PAPEL E TESOURA =====')

print('''[0] - PEDRA \n[1] - PAPEL \n[2] - TESOURA''')

itens = ('PEDRA', 'PAPEL', 'TESOURA')

jogador = int(input('QUAL É A SUA JOGADA: '))
computador = randint(0,2)

print(' ===== JO =====')
sleep(1.0)
print(' ===== KEN ====')
sleep(1.0)
print(' ===== PO =====')

if jogador == 0 and computador == 2 or jogador == 1 and computador == 0 or jogador == 2 and computador == 1:
    print('VOCÊ VENCEU, VOCÊ JOGOU {} E O COMPUTADOR JOGOU {}'.format(itens[jogador], itens[computador]))

elif jogador == 0 and computador == 1 or jogador == 1 and computador == 2 or jogador == 2 and computador == 0:
    print('VOCÊ PERDEU, VOCÊ JOGOU {} E O COMPUTADOR JOGOU {}'.format(itens[jogador], itens[computador]))

elif jogador == computador:
    print('O JOGO EMPATOU, VOCÊ JOGOU {} E O COMPUTADOR JOGOU {}'.format(itens[jogador], itens[computador]))
