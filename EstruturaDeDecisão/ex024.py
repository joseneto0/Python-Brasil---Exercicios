valor_1 = int(input('Digite o 1° valor: '))
valor_2 = int(input('Digite o 2° valor: '))
while True:
    print('[A] - PAR ou ÍMPAR')
    print('[B] - POSITIVO ou NEGATIVO')
    print('[C] - INTEIRO ou DECIMAL')
    print('[D]- ENCERRAR PROGRAMA')
    escolha = input().upper()
    print('-=' * 30)
    if escolha != 'D':
        if escolha == 'A':
            if valor_1 % 2 == 0 and valor_2 % 2 == 0:
                print('Os dois valores são pares')
            elif valor_1 % 2 == 0 and valor_2 % 2 != 0:
                print(f'Apenas o valor {valor_1} é par')
            elif valor_1 % 2 != 0 and valor_2 % 2 == 0:
                print(f'Apenas o valor {valor_2} é par')
            else:
                print('Os dois valores são ímpares')
        elif escolha == 'B':
            if valor_1 > 0 and valor_2 > 0:
                print('Os dois valores são positivos')
            elif valor_1 > 0 and valor_2 < 0:
                print(f'Apenas o valor {valor_1} é positivo')
            elif valor_1 < 0 and valor_2 > 0:
                print(f'Apenas o valor {valor_2} é positivo')
            else:
                print('Os dois valores são negativos')
        elif escolha == 'C':
            if valor_1 // 1 == valor_1 and valor_2 // 1 == valor_2:
                print('Os dois valores são inteiros')
            elif valor_1 // 1 == valor_1 and valor_2 // 1 != valor_2:
                print(f'Apenas o valor {valor_1} é inteiro')
            elif valor_1 // 1 != valor_1 and valor_2 // 1 == valor_2:
                print(f'Apenas o valor {valor_2} é inteiro')
            else:
                print('Os dois valores são decimais')
    else:
        break