sexo = str(input('Informe seu sexo: [M/F] ')).upper()
while sexo not in 'MF':
    sexo = str(input('dados invalidos, digite seu sexo: [M/F]')).upper

print('sexo {} resgistrado com sucesso'.format(sexo))

