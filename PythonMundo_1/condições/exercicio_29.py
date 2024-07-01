velocidade = int (input())
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('voce excedeu a velocidade maxima permitida de 80Km/h')
    print('voce deve pagar uma multa de {:.2f}'.format(multa))
else:
    print('tenha um bom dia, dirija com segurança')