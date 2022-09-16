mulhermenos20 = mais18 = homens = 0

while True:
    print(' === CADASTRE UMA PESSOA ===')
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO[M/F]: '))
   
    while sexo not in 'MmFf':
        sexo = str(input('SEXO[M/F]: '))
   
    continuar = str(input(' === CONTINUAR[S/N]:'))
   
    while continuar not in 'SsNn':
        continuar = str(input(' === CONTINUAR[S/N]:'))

    if idade > 18:
        mais18 += 1

    if sexo in 'Ff' and idade < 20:
        mulhermenos20 += 1

    if sexo in 'Mm':
        homens += 1

    if continuar in 'Nn':
        print('PESSOAS COM MAIS DE 18 ANOS: {}'.format(mais18))
        print('HOMENS CADASTRADOS: {}'.format(homens))
        print('MULHERES MENORES DE 20 ANOS: {}'.format(mulhermenos20))
        break




