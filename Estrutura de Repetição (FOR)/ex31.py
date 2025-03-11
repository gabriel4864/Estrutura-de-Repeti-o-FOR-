# Contar Números Pares em uma Lista
# Dada uma lista de números, conte e exiba quantos são pares.

numero = [2, 4, 4, 3, 9]
contador = 0
for n in numero:
    if n % 2 == 0:
        contador += 1
print(f"A lista {numero} possui {contador} valores pares")