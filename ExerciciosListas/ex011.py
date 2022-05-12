lista1 = []
lista2 = []
lista3 = []
lista4 = []
print('Primeira lista')
for i in range(1, 11):
    lista1.append(int(input(f'{i}° - Digite um elemento: ')))

print('Segunda lista')
for i in range(1, 11):
    lista2.append(int(input(f'{i}° - Digite um elemento: ')))

print('Terceira lista')
for i in range(1, 11):
    lista3.append(int(input(f'{i}° - Digite um elemento: ')))

for i in range(10):
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])
print(f'Valores intercalados: {lista4}')