print('===== TABUADA USANDO O LAÇO FOR =====')

num = float(input('DIGITE UM NUMERO PARA VER SUA TABUADA: '))

c = 0

for c in range(1,10):
    print(' {:.2f} x {} = {:.2f}'.format(num, c, c*num))