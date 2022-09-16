cont = num = 0
produto = 1

while True:
    num = int(input('DIGITE UM NUMERO PARA VER SUA TABUADA[N° 0 PARA SAIR]: '))
    
    if num == 0:
        print('PROGRAMA ENCERRADO.')
        break
    
    for cont in range(0, 9):
        cont += 1
        produto = num * cont
        print('{} x {} = {}'.format(num, cont, produto))
