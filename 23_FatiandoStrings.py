print('===== ANALISADOR DE NOME DE CIDADE SE A MESMA COMEÇA COM SANTO [T/F]')

cidade = str(input('DIGITE O NOME DE UMA CIDADE: ')).strip().upper().lower()

print(cidade[:5] == 'santo')