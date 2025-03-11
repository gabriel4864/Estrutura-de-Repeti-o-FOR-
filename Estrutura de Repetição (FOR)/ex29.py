# Contar Vogais
# Peça ao usuário para digitar uma palavra e exiba quantas vogais ela contém.

palavra= input("Digite uma palavra:"). lower()
vogais = "aeiou"
contador= 0

for letra in palavra:
    if letra in vogais:
        contador += 1
print(f"A palavra {palavra} tem {contador} vogais")