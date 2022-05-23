defeitos = [[], [], [], []]
while True:
    numero_identificador = int(input('Digite o número de identificação do mouse: [0-encerra] '))
    if numero_identificador == 0:
        break
    print('''Defeitos:
    1 - necessita de esfera
    2 - necessita de limpeza
    3 - necessita de troca de cabo ou conectar
    4 - quebrado ou inutilizado''')
    defeito = int(input('Digite o número do defeito: '))
    while defeito < 1 or defeito > 4:
        defeito = int(input('NÚMERO INVÁLIDO! Digite o número do defeito: '))
    print('-=' * 20)
    if defeito == 1:
        defeitos[0].append(defeito)
    elif defeito == 2:
        defeitos[1].append(defeito)
    elif defeito == 3:
        defeitos[2].append(defeito)
    else:
        defeitos[3].append(defeito)
soma_total = defeitos[0].count(1) + defeitos[1].count(2) + defeitos[2].count(3) + defeitos[3].count(4)
print(f'Quantidade de mouses: {soma_total}')
print()
print(f'''Situação                                                     Quantidade                       Percentual
    1 - necessita de esfera                                           {defeitos[0].count(1)}                            {defeitos[0].count(1) * 100 / soma_total:.1f}%
    2 - necessita de limpeza                                          {defeitos[1].count(2)}                            {defeitos[1].count(2) * 100 / soma_total:.1f}%
    3 - necessita de troca de cabo ou conectar                        {defeitos[2].count(3)}                            {defeitos[2].count(3) * 100 / soma_total:.1f}%
    4 - quebrado ou inutilizado                                       {defeitos[3].count(4)}                            {defeitos[3].count(4) * 100 / soma_total:.1f}%''')