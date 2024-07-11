peso = float(input('Qual o seu peso:'))
altura = float(input('Qual a sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu imc é {:.0f}, esta abaixo do peso'.format(imc))
elif imc > 18.4 and imc <= 25:
    print('Seu imc é {:.0f}, esta no peso ideal'.format(imc))
elif imc > 25.0 and imc <= 30:
    print('Seu imc é {:.0f}, esta com sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu imc é {:.0f}, esta com obesidade'.format(imc))
else: 
    print('Seu imc é {:.0f}, esta obesidade morbida'.format(imc))
