lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    if len(lista) == 5:
        break
print(f'Valores digitados: {lista}')