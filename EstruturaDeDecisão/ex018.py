d1, d2, d3 = map(int, input('Digite a data com padrao dd/mm/aaaa: ').split('/'))
if d1 > 31 or d1 == 0 or d1 < 0 or d2 > 12 or d2 == 0 or d2 < 0 or d3 < 0:
    print('Data não válida')
else:
    print('Data válida')