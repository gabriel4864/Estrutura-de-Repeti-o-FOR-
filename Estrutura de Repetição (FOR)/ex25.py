# Contar Números Negativos

numero = [-4, -3, 7, 8, -6]
contador = 0

for n in numero:
    if n <0:
        contador += 1
print(f"A lista {numero} possui {contador} valores negativos")