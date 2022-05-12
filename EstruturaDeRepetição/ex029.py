print('-=' * 20)
print('Lojas Quase Dois - Tabela de preços')
for i in range(1, 51):
    preço = 1.99
    print(f'{i} - {preço * i:.2f}')
levar = int(input('Quantos você vai levar? '))
print(f'Você vai pagar R$ {levar * 1.99:.2f}')
print('-=' * 20)    