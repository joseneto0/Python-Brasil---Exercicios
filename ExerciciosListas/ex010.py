lista1 = []
lista2 = []
lista3 = []
for i in range(10):
    lista1.append(int(input('Digite um elemento: ')))

for i in range(10):
    lista2.append(int(input('Digite um elemento: ')))

for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
print(f'Valores intercalados: {lista3}')