valor_casa = float(input('Valor da casa R$'))
salario = float(input('salario do comprado R$'))
anos = int(input('quantos anos de financiamento?  '))
prestacao = valor_casa/(anos*12)
salario30 = salario*0.3

if prestacao < salario30:
    print('para pagar a casa de R${:.2f} em {} anos a pestração sera de R${:.2f}'.format(valor_casa,anos,prestacao))
    print('emprestimo concedido!!!')
else:
    print('para pagar a casa de R${:.2f} em {} anos a pestração sera de R${:.2f}'.format(valor_casa,anos,prestacao))
    print('emprestimo negado!!!')
