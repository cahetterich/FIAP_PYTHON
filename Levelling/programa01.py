# Exibe "Meu primeiro programa"
print("Meu primeiro Programa")
# Exibe o número 12
print(12)

nome = "Edson"
idade = 48
peso = 85.64

# Forma 1
print("1. O meu nome é", nome, "tenho", idade, "anos e ", peso, "Quilos")

# Forma 2
print("2. O meu nome é {} tenho {} anos e {} Quilos".format(nome, idade, peso))
print("2. O meu nome é {0} tenho {1} anos e {2:.1f} Quilos".format(nome, idade, peso))
print("2. O meu nome é {n} tenho {i} anos e {p:.2f} Quilos".format(n=nome,i=idade,p=peso))

# Forma 3
print(f"3. O meu nome é {nome} tenho {idade} anos e {peso:.2f} Quilos")



# Pede a digitação do salário ao usuário
salario = input("Digite o seu salário:")
salario = float(salario)
# Exibe o salário digitado
print("Salário = R$", salario)



# Calcular
valor1 = 5
valor2 = 3
valor3 = 2
resposta = valor1 + valor2 * valor2 	# Resulta 11
resposta1 = (valor1 + valor2) * valor2	# Resulta 16
valor1 = 17
valor2 = 7
resposta2 = valor1 % valor2		# Resulta 3
resposta3 = valor1 // valor2		# Resulta 2
resposta4 = valor1 / valor2		# Resulta 2.428
resposta5 = 2 ** 4		        # Resulta 16


# Solicita quatro números ao usuário - calcular média
print("Digite 4 números:")
n1 = input()
n1 = float(n1)
n2 = float(input())
n3 = float(input())
n4 = float(input())
# Calcula a média dos 4 números
media = (n1 + n2 + n3 + n4) / 4
print("Média = ", media)



# Solicitando os dados ao usuário
preco_maco = float(input("Digite o preço do maço: "))
qtd_maco = float(input("Digite a quantidade de maços:"))
anos = float(input("Digite a qtd. de anos que fuma:"))
# calcula a qtd. de dias como fumante
dias_fumante = anos * 365
# calcula o gasto do tempo que fuma
custo = dias_fumante * preco_maco
# Exibe o custo
print("Você já gastou R$ ", custo, "Fumando")




# Solicita a quantia
quantia = int(input("Digite a quantia: "))
# Efetua o cálculo das quantias de cédulas
ced50 = quantia // 50
quantia = quantia % 50
ced20 = quantia // 20
quantia = quantia % 20
ced10 = quantia // 10
quantia = quantia % 10
# Exibe as quantidades de cédulas
print("Quantidade das cédulas 50: ", ced50)
print("Quantidade das cédulas 20: ", ced20)
print("Quantidade das cédulas 10: ", ced20)