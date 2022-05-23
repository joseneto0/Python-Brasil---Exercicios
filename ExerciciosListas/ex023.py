nomes = []
bytes = []
for i in range(6):
    nome, b = input('Nome e tamanho em bytes: ').split()
    b = int(b)
    nomes.append(nome)
    bytes.append(b)
total = sum(bytes) / 1048576
print('')
print('ACME Inc.              Uso do espaço em disco pelos usuários')
print('--' * 20)
print('Nr.  Usuário           Espaço Utilizado          % de uso')
for i in range(6):
    print(f'{i+1} {nomes[i]:6} {bytes[i] / 1048576:5.1f} {(bytes[i] / 1048576) * 100 / total:.2f}%')

# ta feio, mas ta funcional