print(' ===== Banco Cev =====')
valor = float(input('DIGITE O VALOR PARA SAQUE: R$ '))
totced50 = totced20 = totced10 = totced1 = 0

while True:
   
    if valor >= 50:
        totced50 += 1
        valor -= 50
    else:
    
        if valor >= 20:
            totced20 += 1
            valor -= 20
        else:
        
            if valor >= 10:
                totced10 += 1
                valor -= 10
            else:
              
                if valor >= 1:
                    totced1 += 1
                    valor -= 1
              
                if valor == 0:
                    break

print('DISPONIBILIZADO {} CEDULAS DE R$ 50.00'.format(totced50))
print('DISPONIBILIZADO {} CEDULAS DE R$ 20.00'.format(totced20))
print('DISPONIBILIZADO {} CEDULAS DE R$ 10.00'.format(totced10))
print('DISPONIBILIZADO {} CEDULAS DE R$ 1.00'.format(totced1))



