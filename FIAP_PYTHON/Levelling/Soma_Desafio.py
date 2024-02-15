#somar números maiores que 10, e se incluido um número negativo,
# o programa deve somar as quantidades.

#soma = 0

#num = int(input("Digite um número maior que 10: "))

#while num < 10:
#   print("Número inválido!")
#   num = int(input("Digite um número maior que 10: "))

#   if num >= 0:
#       soma = soma + num
 #   else:
#      break

#print("Soma = ", soma)

soma = 0

while True:
    num = int(input("Digite um número maior que 10: "))
    if num <= 10:
        print("Número inválido!")
    else:
        soma += num
        print("Novo número adicionado: ", num)
        print("Soma atual: ", soma)
        print("Deseja continuar? (s/n)")
        if input() != 's':
            break

print("Soma final: ", soma)