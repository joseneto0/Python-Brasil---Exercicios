def valorPagamento(prestacao, dias):
    if dias == 0:
        return f'Valor a pagar: R$ {prestacao:.2f}'
    else:
        multa = prestacao * (3/100) + dias * (0.1/100) 
        return multa


#prog principal
prest = []
while True:
    prestacao = float(input('Digite o valor da prestacao: [0-encerrar] '))
    if prestacao == 0:
        break
    dias = int(input('Digite a quantos dias a prestacao está atrasada: '))
    prest.append(valorPagamento(prestacao, dias) + prestacao)
    print(f'Você vai pagar R$ {valorPagamento(prestacao, dias) + prestacao:.2f}')
if len(prest) > 0:
    print('=' * 20)
    print('Relátorio Diário'.center(20))
    print('=' * 20)
    for e, i in enumerate(prest):
        print(f'Prestação {e+1} - R$ {i:.2f}')
    print(f'Total a ser pago: R$ {sum(prest):.2f}')
else:
    print('Você não pagou nada hoje')