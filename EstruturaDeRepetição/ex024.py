soma = 0
qntd_notas = 0
while True:
    notas = int(input('Digite sua nota: '))
    while notas < 0 or notas > 10:
        notas = int(input('Digite sua nota: [0-10] '))
    soma += notas
    qntd_notas += 1
    continuar = input('Quer continuar? [S/N] ')
    if continuar in 'Nn':
        break
print(f'Sua média é {soma / qntd_notas:.2f}')