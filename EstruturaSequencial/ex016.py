from math import ceil
area_para_pintar = int(input('Área em m² que vai ser pintada: '))
lata = 18 * 3
latas_comprar = area_para_pintar / lata
latas_comprar = ceil(latas_comprar)
preco_total = latas_comprar * 80
print('Você precisará de {:.0f} latas para pintar sua loja'.format(latas_comprar))
print('Você irá gastar R$ {:.2f} para pinta sua loja'.format(preco_total))