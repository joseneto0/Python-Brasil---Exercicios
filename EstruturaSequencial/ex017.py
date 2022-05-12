from math import ceil
from math import floor
area_para_pintar = int(input('Área em m² que vai ser pintada: '))
lata = 18 * 6
galao = 3.6 * 6
latas_comprar = area_para_pintar / lata
latas_comprar = ceil(latas_comprar)
galoes_comprar = area_para_pintar / galao
galoes_comprar = ceil(galoes_comprar)
print('Você poderá comprar {} latas e custará R$ {}'.format(latas_comprar, latas_comprar * 80))
print('Você pode comprar {} galões e custará R$ {}'.format(galoes_comprar, galoes_comprar * 25))
