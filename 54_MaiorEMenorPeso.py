print('====== EXERCICIO SOBRE O MAIOR E O MENOR PESO ======')

maior = 0
menor = 0

for p in range(1, 6):
    peso = int(input('DIGITE SEU PESO {}° PESSOA: '.format(p)))

    if p == 1:
        maior = peso
        menor = peso
    else:

        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O MAIOR PESO É {} KG'.format(maior))
print('O MENOR PESO É {} KG'.format(menor))