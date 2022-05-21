def percentual(v, s):
    calculo = v * 100 / s
    print(f' {repetido[i]} {votos_individual:9} {calculo:9}%')


print('Enquete: Quem foi o melhor jogador?')
votos = []
repetido = []
repeticao = 0
while True:
    numero_jogador = int(input('Número de jogador (0=fim) : '))
    votos.append(numero_jogador)
    if numero_jogador == 0:
        break
    while numero_jogador < 0 or numero_jogador > 23:
        votos.remove(numero_jogador)
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
        numero_jogador = int(input('Número de jogador (0=fim) : '))
        votos.append(numero_jogador)

votos.remove(0)      
print()
print('Resultado da votação')
print()
print(f'Foram computados {len(votos)} votos.')
print()
print('Jogador Votos %')
for r in votos:
    if r not in repetido:
        repetido.append(r)
    else:
        pass
repetido.sort()
votos.sort()
soma_votos = 0
for s in range(len(repetido)):
    soma_votos += votos.count(repetido[s])
for i in range(len(repetido)):
    votos_individual = votos.count(repetido[i])
    percentual(votos_individual, soma_votos)