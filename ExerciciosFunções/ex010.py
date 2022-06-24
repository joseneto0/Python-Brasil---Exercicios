from random import randint
from time import sleep
def craps(dado):
    if dado == 7 or dado == 11:
        return 0
    elif dado == 2 or dado == 3 or dado == 12:
        return 1
    else:
        return 2


#prog principal
qntd = 0
tentativas = 0
while True:
    dado = randint(2, 12)
    print(f'Esté é o número sorteado: {dado}')
    sleep(1)
    if tentativas > 0:
        print(f'Tentativas = {tentativas}')
    sleep(1)
    if qntd == 0:
        if craps(dado) == 0:
            print('\033[1;32mNatural. Você ganhou :D\033[m')
            break
        elif craps(dado) == 1 and qntd == 0:
            print('\033[1;31mCraps. Você perdeu :C\033[m')
            break
        elif craps(dado) == 2:
            ponto = dado
            print(f'\033[1;34mEste é o seu ponto: {ponto}, se você achar o número 7 você perde\033[m')
    if qntd > 0:
        print(f'\033[1;34mEste é o seu ponto: {ponto}, se você achar o número 7 você perde\033[m')
        sleep(1)
        if ponto == dado:
            print('\033[1;32mVocê ganhou :D\033[m')
            break
        elif dado == 7:
            print('\033[1;31mVocê perdeu :C\033[m')
            break
    qntd += 1
    tentativas += 1