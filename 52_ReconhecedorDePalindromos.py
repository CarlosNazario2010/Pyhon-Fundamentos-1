from time import sleep

print(' ')
print('===== RECONHECEDOR DE PALÍNDROMOS =====')
print(' ')

frase = str(input('   DIGITE UMA FRASE: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
reverso = ''

for letra in range(len(junto)-1, -1, -1):
    reverso = reverso + junto[letra]

print(' ')
print(   'PROCESSANDO. . .')
sleep(1.5)

if reverso == junto:
    print('O REVERSO DE {} É {} === A PALAVRA É UM PALÍNDROMO'.format(junto, reverso))
else:
    print('O REVERSO DE {} É {} === A PALAVRA NÃO É UM PALÍNDROMO'.format(junto, reverso))




