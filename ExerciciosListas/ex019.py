def mostrarLinha():
    print('--' * 20)


def percentual(total, votos_cada):
    calculo = votos_cada * 100 / total
    print(f'{calculo:>9.2f}%')    


def percentual_final(total, votos_cada):
    calculo = votos_cada * 100 / total
    print(f'{calculo:.2f}%',end='')  


#cod principal
print('"Qual o melhor Sistema Operacional para uso em servidores?"')
print()
print('As possíveis respostas são: ')
print()

#todos os sitemas
sistemas = {
    "nome_windows": 'Windows Server',
    "cod_windows": 1,
    "votos_windows": 0,
    "nome_unix": 'Unix',
    "cod_unix": 2,
    "votos_unix": 0,
    "nome_linux": 'Linux',
    "cod_linux": 3,
    "votos_linux": 0,
    "nome_netware": 'Netware',
    "cod_netware": 4,
    "votos_netware": 0,
    "nome_macos": 'Mac OS',
    "cod_macos": 5,
    "votos_macos": 0,
    "nome_outro": 'Outro',
    "cod_outro": 6,
    "votos_outro": 0,
    "votos_total": []
}

#mostrando as informações dos sistemas para iniciar a votação
print(f'{sistemas["cod_windows"]} - {sistemas["nome_windows"]}')
print(f'{sistemas["cod_unix"]} - {sistemas["nome_unix"]}')
print(f'{sistemas["cod_linux"]} - {sistemas["nome_linux"]}')
print(f'{sistemas["cod_netware"]} - {sistemas["nome_netware"]}')
print(f'{sistemas["cod_macos"]} - {sistemas["nome_macos"]}')
print(f'{sistemas["cod_outro"]} - {sistemas["nome_outro"]}')

#inicio da votação
while True:
    votos = int(input('Digite seu voto: [0-encerra] '))
    while votos < 0 or votos > 6:
        votos = int(input('Tente Novamente. Digite seu voto: [0-encerra] '))
    sistemas["votos_total"].append(votos)
    if votos == 0:
        break
    sistemas["votos_windows"] = sistemas["votos_total"].count(1)
    sistemas["votos_unix"] = sistemas["votos_total"].count(2)
    sistemas["votos_linux"] = sistemas["votos_total"].count(3)
    sistemas["votos_netware"] = sistemas["votos_total"].count(4)
    sistemas["votos_macos"] = sistemas["votos_total"].count(5)
    sistemas["votos_outro"] = sistemas["votos_total"].count(6)
sistemas["votos_total"].remove(0)

#mostrando o resultado da votação
total_votos = sistemas["votos_windows"] + sistemas["votos_unix"] + sistemas["votos_linux"] + sistemas["votos_netware"] + sistemas["votos_macos"] + sistemas["votos_outro"]
print()
print(f'{"Sistema Operacional":25} {"Votos":10} {"%"}')
mostrarLinha()
print(f'{sistemas["nome_windows"]:15} {sistemas["votos_windows"]:13}', end=' ')
percentual(total_votos, sistemas["votos_windows"])

print(f'{sistemas["nome_unix"]:15} {sistemas["votos_unix"]:13}', end=' ')
percentual(total_votos, sistemas["votos_unix"])

print(f'{sistemas["nome_linux"]:15} {sistemas["votos_linux"]:13}', end=' ')
percentual(total_votos, sistemas["votos_linux"])

print(f'{sistemas["nome_netware"]:15} {sistemas["votos_netware"]:13}', end=' ')
percentual(total_votos, sistemas["votos_netware"])

print(f'{sistemas["nome_macos"]:15} {sistemas["votos_macos"]:13}', end=' ')
percentual(total_votos, sistemas["votos_macos"])

print(f'{sistemas["nome_outro"]:15} {sistemas["votos_outro"]:13}', end=' ')
percentual(total_votos, sistemas["votos_outro"])

mostrarLinha()
print(f'{"Total":15} {total_votos:13}')

#Ganhador
if sistemas["votos_windows"] > sistemas["votos_unix"] and sistemas["votos_windows"] > sistemas["votos_linux"] and sistemas["votos_windows"] > sistemas["votos_netware"] and sistemas["votos_windows"] > sistemas["votos_macos"] and sistemas["votos_windows"] > sistemas["votos_outro"]:
    print(f'O Sistema Operacional mais votado foi o Windows Server, com {sistemas["votos_windows"]} votos, correspondendo a ',end='')
    percentual_final(total_votos, sistemas["votos_windows"])
    print(' dos votos.',end='')
elif sistemas["votos_unix"] > sistemas["votos_windows"] and sistemas["votos_unix"] > sistemas["votos_linux"] and sistemas["votos_unix"] > sistemas["votos_netware"] and sistemas["votos_unix"] > sistemas["votos_macos"] and sistemas["votos_unix"] > sistemas["votos_outro"]:
    print(f'O Sistema Operacional mais votado foi o Unix, com {sistemas["votos_unix"]} votos, correspondendo a ',end='')
    percentual_final(total_votos, sistemas["votos_unix"])
    print(' dos votos.',end='')
elif sistemas["votos_linux"] > sistemas["votos_windows"] and sistemas["votos_linux"] > sistemas["votos_netware"] and sistemas["votos_linux"] > sistemas["votos_macos"] and sistemas["votos_linux"] > sistemas["votos_outro"]:
    print(f'O Sistema Operacional mais votado foi o Linux, com {sistemas["votos_linux"]} votos, correspondendo a ',end='')
    percentual_final(total_votos, sistemas["votos_linux"])
    print(' dos votos.',end='')
elif sistemas["votos_netware"] > sistemas["votos_windows"] and sistemas["votos_netware"] > sistemas["votos_unix"] and sistemas["votos_netware"] > sistemas["votos_linux"] and sistemas["votos_netware"] > sistemas["votos_macos"] and sistemas["votos_netware"] > sistemas["votos_outro"]:
    print(f'O Sistema Operacional mais votado foi o Netware, com {sistemas["votos_netware"]} votos, correspondendo a ',end='')
    percentual_final(total_votos, sistemas["votos_netware"])
    print(' dos votos.',end='')
elif sistemas["votos_macos"] > sistemas["votos_windows"] and sistemas["votos_macos"] > sistemas["votos_unix"] and sistemas["votos_macos"] > sistemas["votos_linux"] and sistemas["votos_macos"] > sistemas["votos_outro"]:
    print(f'O Sistema Operacional mais votado foi o Mac OS, com {sistemas["votos_macos"]} votos, correspondendo a ',end='')
    percentual_final(total_votos, sistemas["votos_macos"])
    print(' dos votos.',end='')
elif sistemas["votos_outro"] > sistemas["votos_windows"] and sistemas["votos_outro"] > sistemas["votos_unix"] and sistemas["votos_outro"] > sistemas["votos_linux"] and sistemas["votos_outro"] > sistemas["votos_netware"] and sistemas["votos_outro"] > sistemas["votos_macos"]:
    print(f'O Sistema Operacional mais votado foi o Outro, com {sistemas["votos_outro"]} votos, correspondendo a ',end='')
    percentual_final(total_votos, sistemas["votos_outro"])
    print(' dos votos.',end='')