print('-=' * 20)
temperaturas = []
for i in range(12):
    temperaturas.append(float(input(f'{i+1}° mês - Temperatura: ')))
media = sum(temperaturas) / len(temperaturas)
print(f'Média anual de temperatura: {media:.1f}°C')
print('Temperaturas acima da média: ')
for i in range(12):
    if temperaturas[i] > media:
        if temperaturas.index(temperaturas[i]) == 0:
            print(f'Janeiro - {temperaturas[i]}°C')
        elif temperaturas.index(temperaturas[i]) == 1:
            print(f'Fevereiro - {temperaturas[i]}°C')
        elif temperaturas.index(temperaturas[i]) == 2:
            print(f'Março - {temperaturas[i]}°C')
        elif temperaturas.index(temperaturas[i]) == 3:
            print(f'Abril - {temperaturas[i]}°C')
        elif temperaturas.index(temperaturas[i]) == 4:
            print(f'Maio - {temperaturas[i]}°C')
        elif temperaturas.index(temperaturas[i]) == 5:
            print(f'Junho - {temperaturas[i]}°C')
        elif temperaturas.index(temperaturas[i]) == 6:
            print(f'Julho - {temperaturas[i]}°C')
        elif temperaturas.index(temperaturas[i]) == 7:
            print(f'Agosto - {temperaturas[i]}°C')
        elif temperaturas.index(temperaturas[i]) == 8:
            print(f'Setembro - {temperaturas[i]}°C')
        elif temperaturas.index(temperaturas[i]) == 9:
            print(f'Outubro - {temperaturas[i]}°C')
        elif temperaturas.index(temperaturas[i]) == 10:
            print(f'Novembro - {temperaturas[i]}°C')
        elif temperaturas.index(temperaturas[i]) == 11:
            print(f'Dezembro - {temperaturas[i]}°C')
print('-=' * 20)