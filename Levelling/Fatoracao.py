# Dado um número pelo usuário, calcular e exibir o seu Fatorial.

# Na Matemática, o Fatorial de um número é a multiplicação
# consecutiva do número até o 1. Por exemplo: 4! = 4 . 3 . 2 . 1 = 24

# Exemplo 1: Então-Faça (While)
n = int(input("Digite um número: "))

fat = 1

while n > 1:
    fat = fat * n
    n = n - 1

print("Fatorial = ", fat)

# Exemplo 2: Então-Enquanto (While True)

n2 = int(input("Digite outro número: "))

fat2 = 1

while True:
    fat2 = fat2 * n2
    n2 = n2 - 1
    if n2 < 1:
        break

print("Fatorial = ", fat2)

# Exemplo 3: Para (FOR)

n3 = int(input("Digite outro número: "))

volta = n3
fat3 = 1

for volta in range(n3, 1, -1):
    fat3 = fat3 * volta

print("Fatorial: ", fat3)