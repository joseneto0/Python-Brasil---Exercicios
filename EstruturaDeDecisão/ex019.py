valor = int(input('Digite o o valor: '))

qntd_unidades = valor % 10
valor = (valor - qntd_unidades) // 10

qntd_dez = valor % 10
valor = (valor - qntd_dez) // 10

qntd_cents = valor

print(f'{qntd_cents} centenas, {qntd_dez} dezenas e {qntd_unidades} unidades')