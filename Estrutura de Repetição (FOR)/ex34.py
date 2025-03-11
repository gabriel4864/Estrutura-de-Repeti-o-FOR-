# Calcular o Fatorial
# Peça para o usuário digitar um número e exiba o fatorial desse número.

num = int(input("Digite um numero: "))
for i in range(num, 1, -1):
    num *= i-1
print(num)