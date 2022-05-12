print('-=' * 20)
preço = float(input('Preço do pão: R$ '))
print('Panificadora Pão de Ontem - Tabela de preços')
for i in range(1, 51):
    print(f'{i} - R$ {preço * i:.2f}')
levar = int(input('Quantos você vai levar? '))
print(f'Você vai pagar R$ {levar * preço:.2f}')
print('-=' * 20) 