n1, n2 = map(int, input('Digite 2 números inteiros: ').split())
n3 = float(input('Digite um número real: '))
a = (n1 * 2) * (n2 / 2)
b = n1 * 3 + n3
c = n3 ** 3
print('O produto do dobro do primeiro com metade do segundo: {}\nA soma do triplo do primeiro com o terceiro: {}\nO terceiro elevado ao cubo: {}'.format(a, b, c))