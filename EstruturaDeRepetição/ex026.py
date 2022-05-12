from time import sleep
lula = 0
bolsonaro = 0
ciro = 0
qntd_votos = 0
total_eleitores = int(input('Quantos eleitores vão votar? '))
print('-=' * 20)
print('             Eleições')
print('-=' * 20)
print('Temos na disputa os candidatos:')
sleep(0.7)
print('[1] - Lula')
sleep(0.7)
print('[2] - Bolsonaro')
sleep(0.7)
print('[3] - Ciro')
while True:
    votos = int(input('Em quem você vai votar? [1-2-3] '))
    qntd_votos += 1
    while votos > 3:
        votos = int(input('Tente Novamente. Em quem você vai votar? [1-2-3] '))
    if votos == 1:
        lula += 1
    elif votos == 2:
        bolsonaro += 1
    else:
        ciro += 1
    if qntd_votos == total_eleitores:
        break
print('-=' * 20)
print('             RESULTADO')
print('-=' * 20)
sleep(0.7)
print(f'Lula: {lula} votos')
sleep(0.7)
print(f'Bolsonaro: {bolsonaro} votos')
sleep(0.7)
print(f'Ciro: {ciro} votos')
print('-=' * 20)
if lula > bolsonaro and lula > ciro:
    print('Lula Venceu!')
elif bolsonaro > lula and bolsonaro > ciro:
    print('Bolsonaro Venceu!')
elif ciro > lula and ciro > bolsonaro:
    print('Ciro venceu!')