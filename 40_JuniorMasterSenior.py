print('===== CATEGORIA DE ATLETAS DE NATAÇÃO =====')

idade = int(input('QUAL A IDADE DO ATLETA: '))

if idade <= 9:
    print('O NADADOR ESTA NA CATEGORIA MIRIM')
elif 9 < idade <= 14:
    print('O NADADOR ESTA NA CATEGORIA INFANTIL')
elif 14 < idade <= 19:
    print('O NADADOR ESTA NA CATEGORIA JUNIOR')
elif 19 < idade <= 25:
    print('O NADADOR ESTA NA CATEGORIA MASTER')
elif idade > 25:
    print('O NADADOR ESTA NA CATEGORIA SÊNIOR')