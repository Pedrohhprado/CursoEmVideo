expr = str(input('digite sua expressão: '))
pilha = []

for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha)==0:
    print('correto')
else:
    print('incorreto')
