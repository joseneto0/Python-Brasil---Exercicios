while True:
    saque = int(input('Digite o quanto você quer sacar? [10|600] '))
    if saque < 10 or saque > 600:
        saque = True
    else:
        notas_100 = saque // 100
        resto = saque % 100

        notas_50 = resto // 50
        resto %= 50

        notas_10 = resto // 10
        resto %= 10

        notas_5 = resto // 5
        resto %= 5

        notas_1 = resto // 1

        print(f'Para sacar a quantia de {saque} reais serão necessárias:')
        print(f'{notas_100} notas de 100, {notas_50} notas de 50, {notas_10} notas de 10, {notas_5} notas de 5 e {notas_1} notas de 1')
        break