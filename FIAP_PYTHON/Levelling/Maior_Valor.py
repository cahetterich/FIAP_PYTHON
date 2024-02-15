#Dados 5 números pelo usuário, exibir o de maior valor

num = int(input("Digite 5 números: "))
maior = num

for cont in range(1,5,1): #começa em 1, vai até o 5 de 1 em 1
    num = int(input())
    if num > maior:
        maior = num
print("Maior valor é = ", maior)