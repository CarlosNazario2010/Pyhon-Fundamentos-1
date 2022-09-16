import random

print('===== SORTEIO DA ORDEM DE APRESENTAÇÃO DE ALUNOS =====')

n1 = str(input('DIGITE O NOME DO PRIMEIRO ALUNO: '))
n2 = str(input('DIGITE O NOME DO SEGUNDO ALUNO: '))
n3 = str(input('DIGITE O NOME DO TERCEIRO ALUNO: '))
n4 = str(input('DIGITE O NOME DO QUARTO ALUNO: '))

lista = [n1,n2,n3,n4]
random.shuffle(lista)

print('A ORDEM DE ESCOLHA DOS ALUNOS FOI: {}'.format(lista))