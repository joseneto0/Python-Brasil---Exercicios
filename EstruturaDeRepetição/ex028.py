qntd_cds = int(input('Quantos CDs você possui em sua coleção? '))
qntd = i = soma = maior = menor = 0
while qntd < qntd_cds:
    valor = float(input(f'{i+1}° - R$ '))
    i += 1
    qntd += 1
    soma += valor
    if qntd == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
media = soma / qntd_cds
print(f'Você gastou em média R$ {media:.2f} por CD')
print(f'O seu CD mais caro custa R$ {maior} e o mais barato R$ {menor}')