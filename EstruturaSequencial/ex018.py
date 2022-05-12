tamanho = int(input('Digite o tamanho do arquivo em MB: '))
velocidade = int(input('Digite a velocidade do seu link de internet em Mbps: '))
tamanho_em_bits = tamanho * 8
tempo_em_segundo = tamanho_em_bits / velocidade
tempo_em_minuto = tempo_em_segundo // 60
tempo_em_segundo = tempo_em_segundo - tempo_em_minuto * 60
print('Seu arquivo demorará {:.0f}:{:.0f} minutos para ser baixado'.format(tempo_em_minuto, tempo_em_segundo))
