import time

print(' ===== EXERCÍCIOS DE MANIPULAÇÃO DE STRINGS =====')

nome = str(input('DIGITE SEU NOME COMPLETO:')).strip()

print('ANALISANDO SEU NOME...')
time.sleep(1.5)

print('SEU NOME EM MAISCULAS É {}'.format(nome.upper()))
print('SEU NOME EM MINUSCULAS É {}'.format(nome.lower()))
print('SEU NOME POSSUI AO TODO {} LETRAS'.format(len(nome)- nome.count(' ')))

separado = nome.split()

print('SEU PRIMEIRO NOME POSSUI {} LETRAS E É {}'.format(len(separado[0]),separado[0].upper()))