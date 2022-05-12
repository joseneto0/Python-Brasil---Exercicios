print('-=' * 28)
print('                      Até 5Kg              Acima de 5Kg')
print('Morango        R$ 2,50 por Kg            R$ 2,20 por Kg') 
print('Maçã           R$ 1,80 por Kg            R$ 1,50 por Kg')
print('-=' * 28)
morango_kilos = int(input('Quantos kgs de morango você irá comprar? '))
maça_kilos = int(input('Quantos kgs de maçã você irá comprar? '))
total_kgs = morango_kilos + maça_kilos
if morango_kilos <= 5:
    morango_valor = morango_kilos * 2.5
else:
    morango_valor = morango_kilos * 2.2
if maça_kilos <= 5:
    maça_valor = maça_kilos * 1.8
else:
    maça_valor = maça_kilos * 1.5
total_valor = morango_valor + maça_valor
if total_kgs > 8 or total_valor > 25.00:
    total_desconto = total_valor - (total_valor * 10/100)
    print(f'Você ganhou um desconto de 10%. Sua compra sairá por R$ {total_desconto:.2f}')
else:
    print(f'Você pagará R$ {total_valor:.2f}')