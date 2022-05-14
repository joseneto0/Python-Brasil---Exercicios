divida = float(input('Digite o valor da dívida: '))
juros = 0.10
print(f'{"Valor da Dívida":6} {"Valor dos Juros":>5} {"Quantidade de Parcelas":>5} {"Valor da Parcela":>5}')
for i in range(0, 13, 3):
    if i == 0:
        print(f'R$ {divida} {"0":>7}% {"1":>14} {"R$ ":>24}{divida / 1:>5}')
    else:
        if i == 3 or i == 6 or i == 9:
            print(f'R$ {divida + divida * juros} {juros*100:>8.0f}% {i:>13} {"R$ ":>24}{(divida + divida * juros)/i:>5.2f}')
            juros += 0.05
        else:
            print(f'R$ {divida + divida * juros} {juros*100:>8.0f}% {i:>14} {"R$ ":>23}{(divida + divida * juros)/i:>3.2f}')
            juros += 0.05