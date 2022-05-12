while True:
    numero = int(input('Digite o número: '))
    continuar = 'S'
    while numero < 0 or numero > 16:
        numero = int(input('Digite o número: [0-16] '))
    print(f'{numero}! = ',end='')
    multiplicador = 1
    for i in range(1, numero + 1):
        multiplicador *= i
    print(f'{multiplicador}')
    continuar = input('Quer continuar? [S/N] ')
    if continuar not in 'Ss':
        break