lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    if len(lista) == 10:
        break
print(f'Valores digitados: {lista}')
lista.reverse()
print(f'Valores digitados em ordem inversa: {lista}')