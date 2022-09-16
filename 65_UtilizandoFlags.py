soma = cont = 0

while True:
    num = int(input('DIGITE UM NUMERO[999 p/ PARAR]: '))
    soma += num
    cont += 1
    
    if num == 999:
        cont -= 1
        soma -= 999
        break

print('VOCE DIGITOU {} NUMEROS E SUA SOMA VALE {}'.format(cont, soma))

