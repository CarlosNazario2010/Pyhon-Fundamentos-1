from datetime import date

print('===== CALENDARIO DE ANO BISSEXTO =====')

ano = int(input('DIGITE O ANO PARA SABER SE É OU NÃO BISSEXTO OU COLOQUE 0 PARA ANALISAR O ANO ATUAL: '))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0) and (ano % 100 != 0):
    print('O ANO {} É BISSEXTO'.format(ano))
else:
    print('O ANO {} NÃO É BISSEXTO'.format(ano))