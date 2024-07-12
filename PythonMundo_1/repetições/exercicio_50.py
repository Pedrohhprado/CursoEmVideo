soma = 0
cont = 0
cont_par = 0
for c in range(1,7):
    cont = cont + 1
    num = int(input('digite o {} valor: '.format(cont)))
    if num % 2 == 0:
       soma += num
       cont_par = cont_par + 1
print('voce informou {} numeros, sendo {} pares e a soma deles é {}'.format(cont,cont_par, soma))
      
        