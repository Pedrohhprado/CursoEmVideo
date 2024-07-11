preco = float(input('preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[1] a vista dinheiro/cheque')
print('[2] a vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartao')
opcao = int(input('Qual a opção? '))

if opcao == 1:
    preco_final = preco - (preco*0.1)
    print('Sua compra de {:.2f} vai custar R${:.2f} no final'.format(preco, preco_final)) 
elif opcao == 2:
    preco_final = preco - (preco*0.05)
    print('Sua compra de {:.2f} vai custar R${:.2f} no final'.format(preco, preco_final)) 
elif opcao == 3:
    preco_final = preco/2
    print('Sua compra de {:.2f} vai custar 2 parcelas de R${:.2f} no final'.format(preco, preco_final)) 
elif opcao == 4:
    parcelas = int(input('quantas parcelas? '))
    preco_1 = preco + (preco*0.2)
    preco_final = preco_1/parcelas
    print('Sua compra de {:.2f} vai custar {} parcelas de R${:.2f} no final'.format(preco,parcelas, preco_final)) 