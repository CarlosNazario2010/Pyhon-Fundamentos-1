from time import sleep

print(' ')
print('====== CALCULADORA DE NÚMEROS PRIMOS =====')
print(' ')

num = int(input('DIGITE UM NÚMERO INTEIRO: '))

print('')
print('PROCESSANDO. . .')
print(' ')
sleep(1.5)

tot = 0

for c in range(1, num + 1):

    if num % c == 0:
        tot = tot + 1

if tot == 2:
    print('O NÚMERO {} É UM NÚMERO PRIMO'.format(num))
else:
    print('O NÚMERO {} NÃO É UM NÚMERO PRIMO'.format(num))
print(' ')
