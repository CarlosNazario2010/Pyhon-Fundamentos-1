print('===== SISTEMA DE PAGAMENTOS =====')

preco = float(input('DIGITE O PREÇO DO PRODUTO: R$ '))

print('''CONDIÇÕES DE PAGAMENTO
[1] - À VISTA EM DINHEIRO COM 10% DE DESCONTO
[2] - À VISTA NO CARTÃO COM 5% DE DESCONTO
[3} - ATÉ DUAS VEZES NO CARTÃO PELO PREÇO À VISTA
[4] - 3 X OU MAIS NO CARTÃO COM 20% DE JUROS AO MÊS''')

pag = int(input('DIGITE UMA OPÇÃO: '))

if pag == 1:
    print('O VALOR DA COMPRA É DE R$: {:.2f}'.format(preco*0.9))
elif pag == 2:
    print('O VALOR DA COMPRA É DE R$: {:.2f}'.format(preco*0.95))
elif pag == 3:
    print('O VALOR DA COMPRA É DE R$: {:.2f} EM DUAS VEZES SEM JUROS'.format(preco/2))
elif pag == 4:
    vezes = int(input('DIGITE EM QUANTAS VEZES DESEJA PARCELAR: '))
    print('O VALOR DA COMPRA É DE R$: {:.2f} EM {} VEZES'.format(preco*1.2/vezes,vezes))