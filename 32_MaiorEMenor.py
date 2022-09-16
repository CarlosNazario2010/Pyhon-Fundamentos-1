num1 = float(input('DIGITE O PRIMEIRO VALOR: '))
num2 = float(input('DIGITE O SEGUNDO VALOR: '))
num3 = float(input('DIGITE O TERCEIRO VALOR: '))

menor = num1
maior = num1

if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3

print('O MENOR VALOR É: {:.2f}'.format(menor))
print('O MAIOR VALOR É {:.2f}'.format(maior))