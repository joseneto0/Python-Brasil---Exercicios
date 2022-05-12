#notas bimestrais
n1, n2, n3, n4 = map(float, input('Digite as 4 notas bimestrais: ').split())
media = (n1 + n2 + n3 + n4) / 4
print('Média: {:.2f}'.format(media))