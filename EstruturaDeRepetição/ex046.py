saltos = []
while True:
    print('-=' * 20)
    atleta = input('Atleta: ')
    if atleta in ' ':
        break
    for i in range(1, 6):
        salto = float(input(f'{i}° Salto: '))
        saltos.append(salto)
    print('-=' * 20)
    print(f'Melhor salto: {max(saltos)} m')
    print(f'Pior salto: {min(saltos)} m')
    saltos.remove(max(saltos))
    saltos.remove(min(saltos))
    print(f'Média dos demais saltos: {sum(saltos) / len(saltos):.1f} m')
    print()
    print(f'Resultado final:\n{atleta}: {sum(saltos) / len(saltos):.1f} m')