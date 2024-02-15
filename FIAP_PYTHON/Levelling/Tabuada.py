# Dado um número pelo usuário, calcular os seus 10 primeiros múltiplos
#  e apresentá-los em formato de tabuada

#Exemplo 1 - Enquanto-Faça (While):

n = int(input("Digite um número: "))

mult = 1
i = 1

while i <= 10:
    mult = i * n
    print(f"{n} X {i} = {mult}")
    i = i + 1


#Exemplo 2 - Faça-Enquanto (Do While):

n2 = int(input("Digite outro número: "))

mult2 = 1
i2 = 1

while True:
    mult2 = i2 * n2
    print(f"{n2} X {i2} = {mult2}")
    i2 = i2 + 1
    if i2 > 10:
        break;

#Exemplo 3 - Para (For):

n3 = int(input("Digite outro número: "))

mult3 = 1

# Laço configurado para 10 voltas
for i3 in range(1, 11, 1):
    mult3 = i3 * n3
    print(f"{n3} X {i3} = {mult3}")