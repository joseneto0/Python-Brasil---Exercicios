A = int(input('Digite o 1° valor: '))
B = int(input('Digite o 2° valor: '))
soma = 0
qntd_numeros = 0
for i in range(A, B+1):
    print(i, end=' ')
    soma += i
    qntd_numeros += 1
print()
media = soma / qntd_numeros
print(f'A média dos valores apresentados é {media}')