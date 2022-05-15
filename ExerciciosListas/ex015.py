notas = []
contador_maior = 0
contador_7 = 0
while True:
    valores = int(input('Digite sua nota: '))
    notas.append(valores)
    if valores == -1:
        break
notas.remove(-1)
print(f'Foram lidos {len(notas)} valores')
print(f'Valores lidos: {notas}')
notas.reverse()
print(f'Valores lidos na ordem inversa: ')
for i in range(len(notas)):
    print(f'{notas[i]}')
notas.reverse()
print(f'Soma dos valores: {sum(notas)}')
print(f'Média dos valores: {sum(notas) / len(notas)}')
for maior in range(len(notas)):
    if notas[maior] > (sum(notas) / len(notas)):
        contador_maior += 1
print(f'Você digitou {contador_maior} valores acima da média')
for l in range(len(notas)):
    if notas[l] < 7:
        contador_7 += 1
print(f'Você digitou {contador_7} valores abaixo de sete')
print('FIM')
print('-=' * 20)