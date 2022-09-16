from datetime import date

print('===== ALISTAMENTO MILITAR =====')

nasc = int(input('DIGITE O ANO DE SEU NASCIMENTO: '))
atual = date.today().year

if atual < nasc + 18:
    print('AINDA FALTAM {} ANOS PARA SEU ALISTAMENTO'.format(nasc+18-atual))
elif atual > nasc + 18:
    print('JÁ SE PASSARAM {} ANOS DO PRAZO PARA SEU ALISTAMENTO'.format(atual - nasc -18))
else:
    print('{} É O ANO DE SEU ALISTAMENTO'.format(atual))