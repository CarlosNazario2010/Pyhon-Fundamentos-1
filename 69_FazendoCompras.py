print('===== LOJA SUPER BARATAO =====')
soma = produtomais1000 = barato = c = 0
nomebarato = ''

while True:
    print('')
    produto = str(input('NOME DO PRODUTO: '))
    preco = float(input('PREÇO DO PRODUTO: '))

    soma = soma + preco

    if preco > 1000:
        produtomais1000 += 1

    c += 1

    if c == 1 or preco < barato:
        barato = preco
        nomebarato = produto

    continuar = str(input('DESEJA CONTINUAR[S/N]: '))
    
    while continuar not in 'SsNn':
        continuar = str(input('DESEJA CONTINUAR[S/N]: '))
   
    if continuar in 'Nn':
        break

print('')
print('O TOTAL DAS COMPRAS FOI DE R$: {} '.format(soma))
print('HÁ {} PRODUTOS COM PREÇO MAIOR DE R$ 1000,00'.format(produtomais1000))
print('O PRODUTO MAIS BARATO É A {} QUE CUSTA {}'.format(nomebarato, barato))
