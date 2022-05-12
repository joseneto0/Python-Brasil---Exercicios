peso = int(input('Peso do peixe: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print('O peso do peixe excedeu em {} kg\nVocê deverá pagar uma multa de R$ {}'.format(excesso, multa))
else:
    print('Seu peixe está dentro do regulamento')