soma = 0
tot20m = 0
maioridadeh = 0
nomevelho = ''

for c in range (1, 5):
    print('==== {}° PESSOA ====='.format(c))
    nome = str(input('NOME: '))
    sexo = str(input('SEXO [M/F]: '))

    while True:
        if sexo in 'MmFf':
            break
        else:
            sexo = str(input('SEXO [M/F]: '))
    
    idade = int(input('IDADE: '))

    soma += idade

    if sexo in 'Ff' and idade < 18:
        tot20m += 1

    if sexo in 'Mm' and maioridadeh < idade:
        maioridadeh = idade
        nomevelho = nome

print('='*30)
print('MEDIA DE IDADE = {} '.format(soma/4))
print('HOMEM MAIS VELHO: {} '.format(nomevelho))
print('QUANTIDADE DE MULHERES COM MENOS DE 20 ANOS: {} '.format(tot20m))