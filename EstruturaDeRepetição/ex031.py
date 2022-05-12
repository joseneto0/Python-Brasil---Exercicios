print('Lojas Tabajara')
soma = 0
i = 1
while True:
    produtos = float(input(f'Produto {i}: R$ '))
    i += 1
    soma += produtos
    if produtos == 0:
        break
print(f'Total: R$ {soma:.2f}')
dinheiro = float(input('Dinheiro: R$ '))
if soma > dinheiro:
    print(f'Troco: R$ {soma - dinheiro}')
else:
    print(f'Troco: R$ {dinheiro - soma}')