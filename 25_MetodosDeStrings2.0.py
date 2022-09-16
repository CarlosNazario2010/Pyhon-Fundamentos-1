print('===== LOCALIZAÇÃO CONTAGEM DE LETRAS EM UMA FRASE =====')

frase = str(input('DIGITE UMA FRASE: ')).upper().strip()

print('A LETRA A APARECE {} VEZES NA FRASE'.format(frase.count('A')))
print('A PRIMEIRA LETRA A APARECE NA POSIÇÃO {}'.format(frase.find('A')+1))
print('A ÚLTIMA LETRA A APARECE NA POSIÇÃO {}'.format(frase.rfind('A')-1))