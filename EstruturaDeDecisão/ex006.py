n1, n2, n3 = map(int, input('Digite 3 números: ').split())
if n1 > 2 and n1 > n3:
    maior = n1
    print('O maior é o {}'.format(maior))
if n2 > n1 and n2 > n3:
    maior = n2
    print('O maior é o {}'.format(maior))
elif n3 > n1 and n3 > n2:
    maior = n3
    print('O maior é o {}'.format(maior))