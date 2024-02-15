# Pede a digitação da idade do usuário
idade = input("Digite sua idade: ")
idade = int(idade)
# Verifica se a idade atende a condição e exibe mensagem
if idade >= 18:
    print("Maior de idade")   # DESVIO COMPOSTO
else:
    print("Menor de idade")