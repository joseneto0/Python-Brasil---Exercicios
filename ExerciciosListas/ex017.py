saltos = []
nome = input('Digite seu nome: ')
for i in range(5):
    saltos.append(float(input(f'Distância do {i+1}° salto: ')))
print('-=' * 20)
print(f'Atleta: {nome}')
print(f'\nPrimeiro Salto: {saltos[0]} m')
print(f'Segundo Salto: {saltos[1]} m')
print(f'Terceiro Salto: {saltos[2]} m')
print(f'Quarto Salto: {saltos[3]} m')
print(f'Quinto Salto: {saltos[4]} m')
print('\nResultado final:')
print(f'Atleta: {nome}')
slts = [str(i) for i in saltos]
print('Saltos: ', end='')
print(' - '.join(slts))
print(f'Média dos saltos: {sum(saltos) / len(saltos)} m')
print('-=' * 20)