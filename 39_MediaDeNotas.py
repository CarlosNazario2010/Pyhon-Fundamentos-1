print('===== CALCULO DE MEDIA DE NOTAS DE ALUNO')

nota1 = float(input('DIGITE A PRIMEIRA NOTA: '))
nota2 = float(input('DIGITE A SEGUNDA NOTA: '))

media = (nota1 + nota2)/2

if media < 5:
    print('SUA MEDIA É {}, REPROVADO'.format(media))
elif 5 <= media <= 6.9:
    print('SUA MEDIA É {} E VOCÊ ESTA EM RECUPERAÇÃO'.format(media))
elif media >= 7:
    print('SUA MEDIA É {}, APROVADO'.format(media))