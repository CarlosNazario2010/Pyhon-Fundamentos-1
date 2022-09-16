print('===== CALCULO DE INDICE DE MASSA CORPORAL =====')

peso = float(input('DIGITE SEU PESO [KG]: '))
altura = float(input('DIGITE SUA ALTURA [M]: '))

imc = peso/altura**2

if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO IDEAL - IMC = {:.2f}'.format(imc))
elif 18.5 <= imc <= 25:
    print('VOCÊ ESTÁ NO PESO IDEAL - IMC = {:.2f}'.format(imc))
elif 25 < imc <= 30:
    print('VOCÊ ESTÁ COM SOBREPESO - IMC = {:.2f}'.format(imc))
elif 30 < imc <= 40:
    print('VOCÊ ESTÁ COM OBESIDADE - IMC = {:.2f}'.format(imc))
elif imc >= 40:
    print('VOCÊ ESTÁ COM OBESIDADE MORBIDA - IMC = {:.2f}'.format(imc))