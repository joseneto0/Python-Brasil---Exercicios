while True:
    numeros = int(input('Digite um número: '))
    while numeros > 100 or numeros < 0:
        numeros = int(input('Tente Novamente. Digite um número: [0-100] '))
    if numeros == 0:
        break
    elif numeros > 0 and numeros <= 25:
        print('Intervalo [0-25]')
    elif numeros > 25 and numeros <= 50:
        print('Intervalo [26-50]')
    elif numeros > 50 and numeros <= 75:
        print('Intervalo [51-75]')
    else:
        print('Intervalo [76-100]')