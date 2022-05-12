litros = int(input('Quantos litros você irá colocar? '))
combustivel = input('[A] - Álcool\n[B] - Gasolina\n')
if combustivel in 'Aa':
    if litros <= 20:
        valor = litros * 1.9 - ((litros * 1.9) * 3/100)
        print(f'Você recebeu um desconto de 3%. Você pagará R$ {valor:.2f}')
    elif litros > 20:
        valor = litros * 1.9 - ((litros * 1.9) * 5/100)
        print(f'Você recebeu um desconto de 5%. Você pagará R$ {valor:.2f}')
elif combustivel in 'Bb':
    if litros <= 20:
        valor = litros * 1.9 - ((litros * 1.9) * 4/100)
        print(f'Você recebeu um desconto de 4%. Você pagará R$ {valor:.2f}')
    elif litros > 20:
        valor = litros * 1.9 - ((litros * 1.9) * 6/100)
        print(f'Você recebeu um desconto de 6%. Você pagará R$ {valor:.2f}')