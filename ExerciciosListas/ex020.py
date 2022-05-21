print('Projeção de Gastos com Abono')
print('=' * 20)
print()
lista = []
abonos = []
minimo = 0
salario = float(input('Salário: '))
while salario != 0:
    lista.append(salario)
    salario = float(input('Salário: '))
print()
print(f'{"Salário":3} {"-"} {"Abono":3}')
for i in lista:
    abono = i * 20 / 100
    if abono < 100:
        print(f'R$ {i:3} {"-"} {"R$ 100.00":3}')
        abonos.append(100.00)
        minimo += 1
    else:
        print(f'R$ {i:3} {"-"} R$ {abono:3.2f}')
        abonos.append(abono)
print()
print(f'Foram processados {len(lista)} colaboradores')
print(f'Total gasto com abonos: R$ {sum(abonos):.2f}')
print(f'Valor mínimo pago a {minimo} colaboradores')
print(f'Maior valor de abono pago: R$ {max(abonos):.2f}')