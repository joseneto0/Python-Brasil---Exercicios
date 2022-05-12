l1, l2, l3 = map(int, input('Digite os 3 segmentos: ').split())
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É possível forma um triângulo')
    if l1 == l2 and l2 == l3 and l1 == l3:
        print('Seu triângulo é Equilátero')
    elif l1 == l2 and l1 != l3 and l2 != l3 or l1 == l3 and l2 != l1 and l2 != l3 or l3 == l1 and l2 != l1 and l2 != l3:
        print('Seu triângulo é Isósceles')
    elif l1 != l2 and l1 != l3 and l2 != l3 and l3 != l2:
        print('Seu triângulo é Escaleno')
else:
    print('Não é possível criar um triângulo')