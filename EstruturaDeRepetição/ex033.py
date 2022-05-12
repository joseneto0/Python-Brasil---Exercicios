soma = contador = maior = menor = 0
while True:
    temps = float(input('Digite sua temperatura (°C): '))
    contador += 1
    soma += temps
    if contador == 1:
        maior = menor = temps
    else:
        if temps > maior:
            maior = temps
        elif temps < menor:
            menor = temps
    continuar = input('Deseja continuar? [S/N] ')
    if continuar in 'Nn':
        break
media = soma / contador
print('-=' * 20)
print(f'A menor temperatura apresentada foi {menor}°C')
print(f'A maior temperatura apresentada foi {maior}°C')
print(f'A média das temperaturas foi de {media:.1f}°C')