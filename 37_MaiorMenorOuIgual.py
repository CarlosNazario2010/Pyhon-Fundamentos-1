valor1 = float(input('DIGITE O PRIMEIRO VALOR: '))
valor2 = float(input('DIGITE O SEGUNDO VALOR: '))

if valor1>valor2:
    print('O PRIMEIRO VALOR É MAIOR QUE O SEGUNDO')
elif valor2>valor1:
    print('O SEGUNDO VALOR É MAIOR QUE O PRIMEIRO')
elif valor1==valor2:
    print('AMBOS OS VALORES SÃO IGUAIS')
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')