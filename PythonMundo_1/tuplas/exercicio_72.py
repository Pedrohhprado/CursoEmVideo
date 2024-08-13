numeros = 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

num = int(input('escolha um numero para ler por extenso: '))
num -= 1
print(f'voce digitou o numero {numeros[num]}.')