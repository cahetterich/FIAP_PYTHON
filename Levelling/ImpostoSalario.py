#Dado o salário do funcionário, calcular i Imposto de Renda e Salário líquido de acordo com:

# - Salário até 1900 isento       - 0 %
# - Salário entre 1900.01 e 2800  - 15 %
# - Salário acima de 2800.01      - 27,5 %

#Inicio
    #Escreva "Digite o salario"
    #Leia salario
sal = float(input("Digite o seu salário:"))

# Se sal <= 1900 Então
if sal <= 1900:
# ir = imposto = 0
    ir = 0
#Senão
else:
    #Se sal <= 2800 Então
    if sal <= 2800:   #podemos usar 'elif'
    # imposto = sal * 0.15 #15%
       ir = sal * 0.15

 #Senão
    else:
    # imposto = sal * 0.275 #27,5%
        ir = sal * 0.275
    #fim_se
#Fim_se

#sal_liq = sal - ir
sal_liq = sal - ir
#Escreva "IR: ", ir
print(f"IR: {ir:.2f}")
#Escreva "Salario Líquido:", sal_liq
print(f"Salário Líquido: {sal_liq:.2f}")
#Fim