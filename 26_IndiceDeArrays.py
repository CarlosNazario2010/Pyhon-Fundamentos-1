print('===== INFORMANDO O PRIMEIRO E ULTIMO NOME =====')

nome = str(input('DIGITE O SEU NOME COMPLETO: ')).split()

print('É UM PRAZER TE CONHECER {}'.format(nome))
print('SEU PRIMEIRO NOME É {}'.format(nome[0]))
print('SEU ÚLTIMO NOME É {}'.format(nome[-1]))