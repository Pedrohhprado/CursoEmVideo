pessoas = []
dados = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('peso: ')))

    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1]>mai:
            mai=dados[1]
        if dados[1]<men:
            men=dados[1]



    opcao = str(input('deseja continuar?  [S/N] '))
    pessoas.append(dados[:])
    dados.clear()


    if opcao in 'Nn':
        break

print (f'Ao todo você cadastrou {len(pessoas)}')
for p in pessoas:
    if p[1] == mai:
        print(f'A pessoa com o maior pesso foi {p[0]} com {mai} KG')
    if p[1] == men:
        print(f'A pessoa com o maior pesso foi {p[0]} com {men} KG')