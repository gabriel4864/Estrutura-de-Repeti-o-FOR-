# Substituir Negativos

numero = [-3, -2, 3, 9, -4]
contador = 0

for n in numero:
    if n <0:
        contador += 1
numero[contador] = 0
print("Nova lista")
print(numero)