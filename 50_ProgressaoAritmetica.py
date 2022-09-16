from time import sleep

print(' ')
print('===== CALCULADORA DE PROGRESSÃO ARITMÉTICA =====')
print(' ')

num = int(input('DIGITE O 1° NÚMERO DA PA: '))
razao = int(input('DIGITE A RAZÃO DA PA: '))
termo = int(input('DIGITE QUANTOS TERMOS POSSUI A PA: '))

print(' ')
print('PROCESSANDO RESULTADO...')
sleep(2.0)
print(' ')

print(' {} =>'.format(num), end=' ')

for c in range(1, termo):
    proxterm = num + razao*c
    print('{} =>'.format(proxterm), end=' ')

print('FIM!')