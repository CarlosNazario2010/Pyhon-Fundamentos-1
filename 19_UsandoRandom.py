import random

print('===== SORTEIO DE ALUNOS PARA ALGUMA ATIVIDADE =====')

n1 = str(input('DIGITE O NOME DO PRIMEIRO ALUNO: '))
n2 = str(input('DIGITE O NOME DO SEGUNDO ALUNO: '))
n3 = str(input('DIGITE O NOME DO TERCEIRO ALUNO: '))
n4 = str(input('DIGITE O NOME DO QUARTO ALUNO: '))

lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)

print('O NOME DO ALUNO ESCOLHIDO FOI: {}'.format(escolhido))
