times = 'botafogo', 'fortaleza', 'flamengo', 'palmeiras', 'sao paulo', 'cruzeiro', 'bahia', 'paranaense', 'atletico mineiro', 'vasco gama', 'bragantino', 'juventude', 'gremio', 'criciuma'

print(f'Lista de times do brasileirão {times}')
print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 ultimos são {times[-4:]}')
print(f'times em ordem alfabetica{sorted(times)}')
print(f'o time palmeiras esta na {times.index("palmeiras")+1} posição')