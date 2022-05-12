soma = 0
qntd_numeros = 0
for i in range(1, 6):
    numeros = int(input(f'Informe o {i}° valor: '))
    soma += numeros
    qntd_numeros += 1
media = soma / qntd_numeros
print(f'A média dos valores é de {media}')