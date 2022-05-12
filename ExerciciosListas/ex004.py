lista = []
vogais = ['a', 'e', 'i', 'o', 'u']
cont_vogais = 0
qntd_nomes = 1
while qntd_nomes <= 10:
    nome = input('Digite um caractere: ')
    qntd_nomes += 1
    lista.append(nome)
    if nome in vogais:
        cont_vogais += 1
print(f'Fora digitadas {len(lista) - cont_vogais} consoantes')