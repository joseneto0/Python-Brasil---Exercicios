data = input('Data de Nascimento: ')
mes = int(data[3:5]) - 1
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maior', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print(f'Você nasceu em {data[0:2]} de {meses[mes]} de {data[6:]}')