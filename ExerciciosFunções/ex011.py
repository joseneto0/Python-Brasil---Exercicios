def converterData(d, m, a):
    mes = ''
    if d < 0 or d > 31 or m < 0 or m > 12 or a < 0:
        return 'NULL'
    else:
        if m == 1:
            mes = 'janeiro'
        elif m == 2:
            mes = 'fevereiro'
        elif m == 3:
            mes = 'março'
        elif m == 4:
            mes = 'abril'
        elif m == 5:
            mes = 'maio'
        elif m == 6:
            mes = 'junho'
        elif m == 7:
            mes = 'julho'
        elif m == 8:
            mes = 'agosto'
        elif m == 9:
            mes = 'setembro'
        elif m == 10:
            mes = 'outubro'
        elif m == 11:
            mes = 'novembro'
        elif mes == 12:
            mes = 'dezembro'
        return f'{d} de {mes} de {a}'


#prog principal
dia, mes, ano = map(int, input('Digite a data: ').split('/'))
print(converterData(dia,mes,ano))