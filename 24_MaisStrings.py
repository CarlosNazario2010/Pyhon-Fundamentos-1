print('===== ANALISADOR PARA SABER SE HÁ SILVA NO NOME DA PESSOA =====')

nome = str(input('QUAL É O SEU NOME COMPLETO: ')).strip().upper()

print('VOCÊ POSSUI SILVA NO NOME? {}'.format('SILVA' in nome))