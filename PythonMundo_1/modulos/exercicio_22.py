
nome_completo = input('Digite seu nome:')
print('Analisando seu nome...')

primeiro_nome = nome_completo.split()
num_letras = nome_completo.replace(' ','')

print('Seu nome em maiúsculas é {}'.format(nome_completo.upper()))
print('Seu nome em minusculas é {}'.format(nome_completo.lower()))
print('Seu nome tem {} letras'.format(len(num_letras)))
print("Seu primeiro nome é {}".format(primeiro_nome[0]))
