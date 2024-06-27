frase = '   Curso em Video python  '

print(frase[5:]) # exemplo de fatiamento
print(len(frase)) # conta os caracteres
print(frase.count('o',0,13)) # conta quantos 'o' tem na frase usando fatiamento
print(frase.find('deo')) # encontra a posição do 'deo'
print('Curso' in frase) # indica se a palavra esta na frase

print( frase.replace('python' , 'android') ) # substitui a palavra pra outra
print(frase.upper()) # frase toda maiuscula
print(frase.lower()) # frase toda minuscula
print(frase.capitalize()) # tudo minusculo tirando a primeira letra
print(frase.title()) # começo de cada palavra em maiuculo

print(frase.strip()) # tira os espaços desnesseçarios no começo e fim
print(frase.rstrip()) # remove só os ultimos espaços
print(frase.lstrip()) # remove só os espaços do começo

print(frase.split()) # divide a frase em uma lista separo por espaços
print('-'.join(frase)) # junta a frase usando o separador de sua escolha
