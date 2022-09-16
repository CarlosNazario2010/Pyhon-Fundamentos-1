import math

print('===== CALCULADORA DE SENO, COSSENO E TANGENTE DE UM ÂNGULO')

a = float(input('DIGITE UM ÂNGULO PARA REALIZAR O CÁLCULO: '))

s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print('O SENO DO ÂNGULO É: {:.2f} \nO COSSENO DO ÂNGULO É: {:.2f} \nE A TANGENTE DO ÂNGULO É: {:.2f}'.format(s,c,t))
