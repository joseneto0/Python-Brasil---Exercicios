alto = menor = gordo = magro = qntd = soma_altura = soma_peso = cod_alto = cod_baixo = cod_gordo = cod_magro = 0
print('###### Acedemia do Zézé! ######')
while True:
    print('-=' * 12)
    codigo = int(input('Digite seu código: '))
    if codigo == 0:
        break
    print('------')
    altura = float(input('Digite sua altura: '))
    print('------')
    if qntd == 0:
        alto = menor = altura
        cod_alto = cod_baixo = codigo
    else:
        if altura > alto:
            alto = altura
            cod_alto = codigo
        elif altura < menor:
            menor = altura
            cod_baixo = codigo
    peso = float(input('Digite seu peso: '))
    if qntd == 0:
        gordo = magro = peso
        cod_gordo = cod_magro = codigo
    else:
        if peso > gordo:
            gordo = peso
            cod_gordo = codigo
        elif peso < magro:
            magro = peso
            cod_magro = codigo
    qntd += 1
    soma_altura += altura
    soma_peso += peso
media_altura = soma_altura / qntd
media_peso = soma_peso / qntd

print('-=' * 20)
print(f'Código do cliente mais alto: {cod_alto}\nAltura: {alto}m')
print(f'Código do cliente mais baixo: {cod_baixo}\nAltura: {menor}m')
print(f'Código do cliente mais gordo: {cod_gordo}\nPeso: {gordo}Kg')
print(f'Código do cliente mais magro: {cod_magro}\nPeso: {magro}Kg')
print()
print(f'A média de altura dos nossos alunos ficou de {media_altura:.2f}m')
print(f'A média de peso ficou de {media_peso:.2f} Kg')
print('-=' * 20)