import json

with open("dados.json") as faturamento: 
    dados = json.load(faturamento)
    
valores = [i['valor'] for i in dados if i['valor'] > 0] #cria uma variavel que armazena todos os valores da base de dados que sao maiores que 0
menor = min(valores) #funcao que calcula o minimo
maior = max(valores) #funcao que calcula o maximo

media = sum(valores) / len(valores) #funcao para calculo da media, e abaixo a funcao que soma 1 toda vez que o faturamento for maior que a media
maior_media = sum(1 for i in valores if i > media) 

print('Menor Faturamento: R$', menor)
print('Maior Faturamento: R$', maior)
print('Quantidade de dias em que faturamento foi maior que media: ', maior_media)
