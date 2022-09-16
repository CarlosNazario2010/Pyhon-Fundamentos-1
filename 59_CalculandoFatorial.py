num = int(input('DIGITE O NUMERO PARA CALCULO DO FATORIAL: '))
fat = 1

# USANDO O WHILE

while num > 0:
    print(' {} '.format(num), end='')
    print(' X ' if num > 1 else ' = ', end='')
    fat *= num
    num -= 1

print(' {} '.format(fat))


# USANDO O COMANDO FOR:

#for c in range (num, 0, -1):
#    print(num, end='')
#    fat *= num
#    num -= 1
#print(fat)
