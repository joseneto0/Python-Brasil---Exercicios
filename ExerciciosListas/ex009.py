A = []
while len(A) != 10:
    numeros = int(input('Digite um valor: '))
    numeros **= 2
    A.append(numeros)
print(f'Quadrado dos valores digitados: {A}')
print(f'Soma dos quadrados: {sum(A)}')