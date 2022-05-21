print('Comparativo de Consumo de Combustível')
print()
modelos = ['Fusca', 'Gol', 'Uno', 'Vectra', 'Peugeout']
consumo = [7, 10, 12.5, 9, 14.5]
menor = []
for i in range(len(modelos)):
    print(f'Veículo {i+1}')
    print(f'Nome: {modelos[i]}')
    print(f'Km por litro: {consumo[i]}')
    print()
print('Relatório Final')
for c in range(len(modelos)):
    print(f'{c+1:>3} - {modelos[c]:15} {"-":6} {consumo[c]:5.1f} {"-":2} {1000/consumo[c]:5.1f} litros {"-":2} R$ {1000/consumo[c] * 2.25:.2f}')
    menor.append(1000/consumo[c] * 2.25)
print(f'O menor consumo é do {modelos[menor.index(min(menor))]}.')