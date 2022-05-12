N = int(input('Digite um número: '))
lista = []
cont = 0
for i in range(N+1):
    if i % 2 == 1 and i !=2:
        lista.append(i)
        cont += 1
    else:
        cont += 1
print(f'Números primos entre 1 e {N}: {lista}\nNúmero de divisões: {cont}')

