print('===== CALCULANDO O VALOR DE UMA HIPOTENUSA EM UM TRIÂNGULO RETÂNGULO =====')

co = float(input('DIGITE O VALOR DO CATETO OPOSTO: '))
ca = float(input('DIGITE O VALOR DO CATETO ADJACENTE: '))

h = (co**2+ca**2)**(1/2)

print('O VALOR DA HIPOTENUSA DO TRIÂNGULO RETÂNGULO É: {:.2f}'.format(h))