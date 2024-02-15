# Dados 2 números, exibir os números do intervalo

ini = int(input("Digite o número inicial: "))
f = int(input("Digite o valor final: "))

#for cont in range(ini, f + 1, 1):  # for cont in range(ini + 1, f):
#   print(cont, " ")

#while ini <= f:
#    print(ini, " ")
#    ini = ini + 1 # ini =+ 1

#while True:
#   print(ini, " ")
#   ini = ini + 1 # ini =+ 1
#   if ini > f:
#        break

#ou

def exibir_intervalo(a, b):
    # Garantir que a <= b
    if a > b:
        a, b = b, a
    for i in range(a, b+1):
        print(i)

# Exemplo de chamada da função
exibir_intervalo(11, 11)

#ou 2

def ler_dois_numeros():
    try:
        numero1 = int(input("Digite o primeiro número inteiro: "))
        numero2 = int(input("Digite o segundo número inteiro: "))
    except ValueError:
        print("Erro: um ou ambos os valores inseridos não são números inteiros válidos.")
        return None

    if numero1 > numero2:
        print("Erro: o primeiro número deve ser menor ou igual ao segundo número.")
        return None

    for i in range(numero1, numero2+1):
        print(i)

# Exemplo de chamada da função
ler_dois_numeros()