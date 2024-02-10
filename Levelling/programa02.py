#Escreva "Digite o valor da venda:"
venda = float(input("Digite a venda:"))
#Leia venda #ex: 300
#Se venda > 300 então
if venda > 300:
    # desconto = venda * 10 / 100
    desconto = venda * 10 / 100
    # venda = venda - desconto
    venda = venda - desconto
    # Escreva "Novo valor =", venda
    print("Novo valor = ", venda)

#Número negativo vira positivo

    # Solicita um número digitado pelo usuário
    n = int(input("Digite um número:"))
    # Comando de decisão: Verifica se o número é negativo
    if n < 0:
        n = n * (-1)
    # Exibe o número positivo

    print("Módulo: ", n)