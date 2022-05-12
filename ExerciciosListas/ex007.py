lista = []
mult = 1
while len(lista) != 5:
    valores = int(input('Digite um valor: '))
    mult *= valores
    lista.append(valores)
print(f'Valores digitados: {lista}')
print(f'Soma dos valores: {sum(lista)}')
print(f'Multiplicação dos valores: {mult}')
