sp = 67836.43 #valores informados nas questoes=
rj = 36676.66
mg = 29229.88
es = 27165.48
outros = 19843.53

soma = sp + rj + mg + es + outros #somando os valores para calcular a porcentagem

sp = sp/soma * 100 #calculo das porcentagens individuais
rj = rj/soma * 100
mg = mg/soma * 100
es = es/soma * 100
outros = outros/soma * 100

print("SP: {0:.2f}%".format(sp))
print("RJ: {0:.2f}%".format(rj))
print("MG: {0:.2f}%".format(mg))
print("ES: {0:.2f}%".format(es))
print("Outros: {0:.2f}%".format(outros))
