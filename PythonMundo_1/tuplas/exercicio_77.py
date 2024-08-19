palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar')

for p in palavras:
    print(f'\nNa palvra {p} temos ',end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra,end=' ')
        