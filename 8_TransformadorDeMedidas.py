m = float(input('DIGITE SUA MEDIDA EM METROS: '))

km = m/1000
hm = m/100
cm = m*100
mm = m*1000

print('SUA MEDIDA EM KM É: {} \nSUA MEDIDA EM HM É: {} \nSUA MEDIDA EM CM É: {:.0f} \nSUA MEDIDA EM MM É: {:.0f}'.format(km,hm,cm,mm))