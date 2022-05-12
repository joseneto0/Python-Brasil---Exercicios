A = 80000
B = 200000
qntd_anos = 0
while A != B or A < B:
    A = A + (A * 3/100)
    B = B + (B * 1.5/100)
    qntd_anos += 1
print(f'É preciso {qntd_anos} anos para igualar ou passar a população')