A = int(input('Qual a população inicial de A? '))
taxa_A = float(input('Qual a taxa de crescimento de A? (em %) '))
B = int(input('Qual a população inicial de B? '))
taxa_B = float(input('Qual a taxa de crescimento de B? (em %) '))
qntd_anos = 0
while A != B or A < B:
    A = A + (A * taxa_A/100)
    B = B + (B * taxa_B/100)
    qntd_anos += 1
print(f'É preciso {qntd_anos} anos para igualar ou passar a população')