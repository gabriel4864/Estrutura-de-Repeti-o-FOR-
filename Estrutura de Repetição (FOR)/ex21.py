# Média de Valores
# Solicite que o usuário digite 5 números e exiba a média aritmética deles.

soma=0
for i in range(5):
    num= int(input("Digite 5 números:"))
soma += num
media = soma/5
print(media)