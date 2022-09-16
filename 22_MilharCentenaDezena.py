import time

print('===== ANALISADOR DE ALGARISMOS CARDINAIS =====')

n = int(input('DIGITE UM NÚMERO INTEIRO: '))

print('ANALISANDO O NUMERO DIGITADO...')

u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10

time.sleep(1.5)

print('UNIDADES X {}'.format(u))
print('DEZENAS X {}'.format(d))
print('CENTENAS X {}'.format(c))
print('MILHARES X {}'.format(m))
