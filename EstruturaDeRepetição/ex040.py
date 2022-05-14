soma = menor_indice = maior_indice = cidade_maior_i = cidade_menor_i = indice = soma_menos_2000 = cont = 0
for i in range(5):
    codigo_cidade = int(input(f'{i+1}° - Código da cidade: '))
    num_veiculos = int(input('Número de veículos de passeio: '))
    soma += num_veiculos
    num_acidentes = int(input('Número de acidentes com vítimas: '))
    indice = (num_acidentes / num_veiculos) * 100
    if i == 0:
        maior_indice = menor_indice = codigo_cidade
        cidade_maior_i = cidade_menor_i = indice
    else:
        if indice > cidade_maior_i:
            cidade_maior_i = indice
            maior_indice = codigo_cidade
        elif indice < cidade_menor_i:
            cidade_menor_i = indice
            menor_indice = codigo_cidade
    if num_veiculos < 2000:
        soma_menos_2000 += num_acidentes
        cont += 1
    print('-=' * 12)
print(f'Menor índice de acidentes de transito: {cidade_menor_i:.2f} %. Cidade: {menor_indice}')
print(f'Maior índice de acidentes de transito: {cidade_maior_i:.2f} %. Cidade: {maior_indice}')
print(f'Média de veículos nas 5 cidades juntas: {soma / 5:.2f} veículos')
print(f'A média de acidentes de trabalhos em cidades com menos de 2000 véiculos foi de: {soma_menos_2000 / cont:.2f} acidentes')