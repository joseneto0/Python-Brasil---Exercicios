from math import sqrt
A = int(input('Digite o primeiro valor: '))
if A == 0:
    print('A equação será de primeiro grau. PROGRAMA ENCERRADO')
else:
    B = int(input('Digite o segundo valor: '))
    C = int(input('Digite o terceiro valor: '))
    delta = B**2 - 4 * A * C
    if delta < 0:
        print('Equação não contém raízes reais. PROGRAMA ENCERRADO')
    elif delta == 0:
        x = (-B + sqrt(delta)) / (2 * A)
        print('A equação contém apenas 1 raiz: {}'.format(x))
    else:
        x1 = (-B + sqrt(delta)) / (2 * A)
        x2 = (-B - sqrt(delta)) / (2 * A)
        print('A equação contém duas raizes')
        print('x1 = {}'.format(x1))
        print('x2 = {}'.format(x2))