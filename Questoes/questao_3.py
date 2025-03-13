import json

with open("dados.json") as faturamento:
    dados = json.load(faturamento)
    
valores = [i['valor'] for i in dados if i['valor'] > 0]
menor = min(valores)
maior = max(valores)

media = sum(valores) / len(valores)
maior_media = sum(1 for i in dados if i > media)

print('Menor Faturamento: R$', menor)
print('Maior Faturamento: R$', maior)
print('Quantidade de dias em que faturamento foi maior que media', maior_media)
