from time import sleep

primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
opcao = 0
resultado = 0

while opcao != 5:
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NUMEROS')
    print('[5] SAIR')

    opcao = int(input('>>>>>>> Qual é a sua opção? '))
    
    if opcao == 1:
        resultado = primeiro_valor + segundo_valor
        print('A soma de {} e {} é {}'.format(primeiro_valor,segundo_valor,resultado))
    
    elif opcao == 2:
        resultado = primeiro_valor * segundo_valor
        print('O resultado de {} x {} é {}'.format(primeiro_valor,segundo_valor,resultado))

    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print('Entre {} e {} o maior valor é {}'.format(primeiro_valor,segundo_valor,primeiro_valor))
        else:
            print('Entre {} e {} o maior valor é {}'.format(primeiro_valor,segundo_valor,segundo_valor))

    elif opcao == 4:
        print('Digite os numeros novamente:')
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando programa...')
        sleep(2)
    
    else:
        print('Numero invalido, tente novamente.')

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    sleep(1)

print('Programa finalizado')
