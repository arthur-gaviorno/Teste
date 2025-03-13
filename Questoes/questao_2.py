def testa_numero(x):
    a , b = 0 , 1 #iniciando os dois primeiros numeros da sequencia
    while b < x: 
        a, b = b, a + b #atualiza de forma que o proximo termo e a soma dos dois anteriores
    return b == x or x == 0 #retorna quando o numero da sequencia for igual ao valor, x == 0 adicionado pois pode dar erro no resultado

i =int(input('Digite o numero e vbeja se esta na sequencia: ' )) 

if testa_numero(i): #estrutura condicional para testar se o numero pertence ou nao a sequencia
    print(f'O numero {i} pertence a sequncia de fibonacci')
else:
    print(f'O numero {i} nao pertence a sequncia de fibonacci') 
     
