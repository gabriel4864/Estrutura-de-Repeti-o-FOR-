# Contar uma Letra em uma Frase
#Solicite uma frase e uma letra ao usuário e exiba quantas vezes essa letra aparece na frase.

frase = str(input("Digite uma frase: ")).lower()
letra = str(input("Digite uma letra: ")).lower()
contador = 0
for i in frase:
    if letra in i:
        contador += 1
print(f"A frase: {frase} possui {contador} letras {letra}")