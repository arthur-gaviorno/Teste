def testa_numero(x):
    a , b = 0 , 1
    while b < x:
        a, b = b, a + b
    return b == x or x == 0

i =int(input('Digite o numero e vbeja se esta na sequencia: ' ))

if testa_numero(i):
    print(f'O numero {i} pertence a sequncia de fibonacci')
else:
    print(f'O numero {i} nao pertence a sequncia de fibonacci') 
     