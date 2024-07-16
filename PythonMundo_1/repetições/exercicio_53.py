frase = str(input('digite a frase: '))
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('{} é um palindromo'.format(junto))
else: 
    print('não é um palindromo')