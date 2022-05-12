n1, n2, n3 = map(int, input('Digite os valores: ').split())
if n1 < n2 and n1 < n3:
    menor = n1
    print('Compre o 1° produto com valor de R$ {}'.format(menor))
elif n2 < n1 and n2 < n3:
    menor = n2
    print('Compre o 2° produto com valor de R$ {}'.format(menor))
elif n3 < n1 and n3 < n2:
    menor = n3
    print('Compre o 3° produto com valor de R$ {}'.format(menor))