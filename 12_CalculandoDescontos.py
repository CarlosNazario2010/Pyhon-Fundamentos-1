p = float(input('DIGITE O VALOR DO PRODUTO: R$'))
d = float(input('DIGITE O DESCONTO: %'))

preço = p*(1-d/100)

print('O VALOR DO PRODUTO É R$ {:.2f} \nE COM O DESCONTO DE {}% ELE FICA R$ {:.2f}'.format(p,d,preço))