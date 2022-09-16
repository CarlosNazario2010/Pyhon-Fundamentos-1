print('===== CONVERSOR DE BASES NUMÉRICAS =====')

num = int(input('DIGITE O NÚMERO QUE DESEJA CONVERTER: '))

print('''[1] PARA BINÁRIO
[2] PARA OCTAL
[3] PARA HEXADECIMAL''')

opcao = int(input('DIGITE A OPÇÃO DESEJADA: '))

if opcao == 1:
    print('O BINARIO DE {} É {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O OCTAL DE {} É {:2}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O HEXADECIMAL DE {:2} É {}'.format(num,hex(num)[2:]))
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE.')

