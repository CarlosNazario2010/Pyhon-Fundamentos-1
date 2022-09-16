print('===== ANALISADOR DE TRIANGULOS =====')

s1 = float(input('DIGITE O PRIMEIRO SEGMENTO: '))
s2 = float(input('DIGITE O SEGUNDO SEGMENTO: '))
s3 = float(input('DIGITE O TERCEIRO SEGMENTO: '))

if s1**2 == s2**2 + s3**2 or s2**2 == s1**2 + s3**2 or s3**2 == s1**2 + s2**2:
    print('O TRIANGULO EM QUESTÃO É UM TRIANGULO RETANGULO')
elif s1 + s2 < s3 or s1 + s3 < s2 or s2 + s3 < s1:
    print('OS SEGMENTOS EM QUESTÃO NÃO FORMAM UM TRIANGULO')
elif s1 != s2 != s3:
    print('O TRIANGULO EM QUESTÃO É UM TRIANGULO ESCALENO')
elif s1 == s2 != s3 or s1 == s3 != s2 or s2 == s3 != s1:
    print('O TRIANGULO EM QUESTÃO É UM TRIANGULO ISOCELES')
elif s1 == s2 == s3:
    print('O TRIANGULO EM QUESTÃO É UM TRIANGULO EQUILATERO')

