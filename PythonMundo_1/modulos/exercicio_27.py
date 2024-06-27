nome = str((input('Qual o seu nome?'))).strip()
n = nome.split()
print('seu primeiro nome é {}'.format(n[0]))
print('seu ultimo nome é {}'.format(n[len(n)-1]))