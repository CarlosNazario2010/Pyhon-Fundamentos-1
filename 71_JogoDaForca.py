import getpass               # GETPASS PERMITE ESCONDER O INPUT (NO CASO, PARA DIGITAR A PALAVRA DA FORCA)

print('''      
                           JOGO DA FORCA
''')

palavra_secreta = getpass.getpass('DIGITE UMA PALAVRA SECRETA: ').upper()
letras_acertadas = list('_' for letra in palavra_secreta)

print(letras_acertadas)
print('')

tentativas = 0
erros = 0

while True:

  palpite = input('digite sua letra: ').upper()
  tentativas += 1                                          # REVISAO DE PROGRAMAÇÃO PROCEDURAL
  indice = 0                                               # CONDIÇÕES, LAÇOS E ITERAVEIS (TUPLAS, LISTAS, ETC) 

  if palpite not in palavra_secreta:
    erros += 1
    print(f'VOCE ERROU {erros} VEZ(ES)')

  for letra in palavra_secreta:
    
    if palpite == letra:
      letras_acertadas[indice] = letra
    indice += 1
  
  print('')
  print(letras_acertadas)
  print('')

  if '_' not in letras_acertadas:
    print(f'VOCE ACERTOU A PALAVRA COM {tentativas} TENTATIVAS!!')
    break
  
  elif erros == 6:
    print(f'VOCE SE ENFORCOU. ERROU O PALPITE 6 VEZES!!')
    break