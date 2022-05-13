from time import sleep
tabuada = int(input('Montar a tabuada de: '))
começo = int(input('Começar por: '))
termino = int(input('Terminar em: '))
while começo > termino:
    print('Tente Novamente. Primeiro um valor menor no inicio')
    começo = int(input('Começar por: '))
    termino = int(input('Terminar em: '))

print(f'Vou montar a tabuada de {tabuada} começando em {começo} e terminando em {termino}')
sleep(0.7)
for i in range(começo, termino+1):
    print(f'{tabuada} x {i} = {tabuada * i}')