from time import sleep
zezin = 0
marysleine = 0
semdedo = 0
thawowkey = 0
voto_nulo = 0
voto_branco = 0
print('ELEIÇÕES')
print('-=' * 15)
sleep(0.6)
print('[1] - Zezin do Povão')
sleep(0.6)
print('[2] - Marysleine da Galera')
sleep(0.6)
print('[3] - Sem dedo')
sleep(0.6)
print('[4] - Tha Wow Key')
sleep(0.6)
print('[5] - Voto Nulo')
print('[6] - Voto em branco')
while True:
    voto = int(input('Em quem você vai votar? [0 para encerrar] '))
    if voto == 0:
        break
    while voto < 0 or voto > 6:
        voto = int(input('Número Inválido. Em quem você vai votar? '))
    if voto == 1:
        zezin += 1
    elif voto == 2:
        marysleine += 1
    elif voto == 3:
        semdedo += 1
    elif voto == 4:
        thawowkey += 1
    elif voto == 5:
        voto_nulo += 1
    elif voto == 6:
        voto_branco += 1
print('-=' * 20)
total = zezin + marysleine + semdedo + thawowkey + voto_nulo + voto_branco
print(f'Total de votos = {total}')
print(f'Total - Zezin: {zezin}')
print(f'Total - Marysleine: {marysleine}')
print(f'Total - Sem Dedo: {semdedo}')
print(f'Total - Tha Wow Key: {thawowkey}')
print(f'Votos Nulos: {voto_nulo}')
print(f'Votos em Branco: {voto_branco}')
percent_nulo = (voto_nulo * 100) / total
print(f'Porcentagem de votos nulos: {percent_nulo:.1f}%')
percent_branco = (voto_branco * 100) / total
print(f'Porcentagem de votos brancos: {percent_branco:.1f}%')