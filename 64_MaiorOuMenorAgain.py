resposta = 'S'
soma = c = maior = menor = 0

while resposta in 'Ss':
    num = int(input('DIGITE UM NUMERO: '))
    soma += num
    c += 1
    
    if c == 1:
        maior = menor = num
    else:
    
        if menor > num:
            menor = num
        if maior < num:
            maior = num

    resposta = str(input('QUER CONTINUAR: '))

media = soma/c

print('VOCE DIGITOU {} NUMEROS E A MEDIA É {}'.format(c, media))
print('O MAIOR NUMERO É {} E O MENOR NUMERO É {}'.format(maior, menor))