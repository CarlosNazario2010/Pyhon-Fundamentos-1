valor1 = int(input('DIGITE O PRIMEIRO VALOR: '))
valor2 = int(input('DIGITE O SEGUNDO VALOR: '))

print(' [1] SOMAR\n [2] MULTIPLICAR\n [3] MAIOR\n [4] NOVOS NUMEROS\n [5] SAIR DO PROGRAMA')
opcao = int(input(' DIGITE A OPÇÃO DESEJADA: '))

while opcao != 5:

    if opcao == 1:
        print(' {} + {} = {} '.format(valor1, valor2, valor1 + valor2))
        opcao = int(input(' DIGITE A OPÇÃO DESEJADA: '))
    
    elif opcao == 2:
        print(' {} X {} = {} '.format(valor1, valor2, valor1 * valor2))
        opcao = int(input(' DIGITE A OPÇÃO DESEJADA: '))
    
    elif opcao == 3:

        if valor1 > valor2:
            print(' {} É MAIOR QUE {} '.format(valor1, valor2))
        elif valor1 < valor2:
            print(' {} É MAIOR QUE {} '.format(valor2, valor1))

        opcao = int(input(' DIGITE A OPÇÃO DESEJADA: '))

    elif opcao == 4:
        valor1 = int(input('DIGITE O PRIMEIRO VALOR: '))
        valor2 = int(input('DIGITE O SEGUNDO VALOR: '))
        opcao = int(input(' DIGITE A OPÇÃO DESEJADA: '))

print('PROGRAMA ENCERRADO!!')