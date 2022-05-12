N = int(input('Digite N: '))
maior = 0
menor = 0
soma = 0
qntd_numeros = 0
while qntd_numeros < N:
    numeros = int(input('Digite seu número: '))
    while numeros < 0 or numeros > 1000:
        numeros = int(input('Digite seu número: [0-1000] '))
    soma += numeros
    qntd_numeros += 1
    if qntd_numeros == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        elif numeros < menor:
            menor = numeros  
media = soma / qntd_numeros
print(f'A média dos números é {media}')
print(f'O menor número é o {menor} e o maior é o {maior}')