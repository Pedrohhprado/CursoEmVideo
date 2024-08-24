dados = {'nome':'Pedro','idade':23}
dados['sexo']='M' # adiciona um elemnto ao dicionario
cont = 0

# del dados['idade'] remove o elemnto idade

print(dados['nome']) # pedro
print(dados['idade']) # 23
print(dados['sexo']) # M

filme_star = {'titulo':'Star wars', 
              'ano':1977,
              'diretor':'George Lucas'
            }
filme_avengers = {'titulo':'Avengers',
                  'ano':2012,
                  'diretor':'Joss Whedon'

                 }
filme_matrix = {'titulo':'Matrix',
                  'ano':1999,
                  'diretor':'Wachowski'

                 }

locadora = [filme_star,filme_avengers, filme_matrix] # uma lista com dicionarios dentro

print(filme_star.values()) # retorna todos valores do dicionario
print(filme_star.keys()) # retorna as chaves do dicionario
print(filme_star.items()) # retorna os dois do dicionario

for k, v in filme_star.items():
    print(f'o {k} é {v}')

print(locadora) # retorna toda lista com dicionarios
print(locadora[2]['ano']) # 1999
print(locadora[1]['diretor']) # Joss Whedon

for c in locadora:
    print('='*12,end='')
    print(locadora[cont]['titulo'],end='')
    print('='*12)
    for k, v in locadora[cont].items():
        print(f'o {k} é {v}')




