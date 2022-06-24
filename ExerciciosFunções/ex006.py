def converter24_12(hora):
    if hora > 12 and hora != 24:
        horas = 0
        for i in range(hora):
            if i >= 12:
                horas += 1
        return horas
    elif hora == 24:
        return 0
    else:
        return hora


def apresentarConversao(hora_convertida, minuto):
    return f'{hora_convertida}:{minuto}h'


#prog principal
horas = int(input('Digite as horas: (em notação 24h) '))
hora_convertida = converter24_12(horas)
minutos = int(input('Digite os mninutos: '))
print(f'Hora em notação 12h: {apresentarConversao(hora_convertida, minutos)}')