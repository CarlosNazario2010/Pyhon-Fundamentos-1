sexo = str(input('DIGITE SEU SEXO [M/F}: '))

while True:

    if sexo in 'MmFf':
        break
    else:
        sexo = str(input('DIGITE SEU SEXO [M/F}: '))

print('SEXO {} REGISTRADO COM SUCESSO.'.format(sexo))