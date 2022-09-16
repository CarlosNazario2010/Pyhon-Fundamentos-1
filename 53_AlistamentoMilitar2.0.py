from datetime import date

print(' ===== ALISTAMENTO MILITAR =====')
print('')

nasc = 0
atual = date.today().year
idade = 0

while True:
    nasc = int(input('ANO DO NASCIMENTO: '))
    idade = atual - nasc

    if idade < 18:
        print('')
        print('AINDA FALTA(M) {} ANOS PARA VOCÊ SE ALISTAR'.format(18 - idade))
    if idade == 18:
        print('')
        print('{} É O ANO DE SEU ALISTAMENTO'.format(atual))
    if idade > 18:
        print('')
        print('JÁ SE PASSOU(PASSARAM) {} ANOS DO PRAZO PARA SEU ALISTAMENTO'.format(idade - 18))

    print('')
    denovo = str(input('DESEJA REALIZAR A OPERAÇÃO NOVAMENTE [S/N]: ').upper())
    print('')

    if denovo == 'N':
        break

print('PROGRAMA ENCERRADO')
