n1, n2 = map(int, input('Digite 2 valores: ').split())
if n1 > n2:
    maior = n1
    print('O maior é o {}'.format(n1))
else:
    print('O maior é o {}'.format(n2))