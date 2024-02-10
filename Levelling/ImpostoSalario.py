#Dado o salário do funcionário, calcular i Imposto de Renda e Salário líquido de acordo com:

# - Salário até 1900 isento       - 0 %
# - Salário entre 1900.01 e 2800  - 15 %
# - Salário acima de 2800.01      - 27,5 %

#var
    #sal: real
#Inicio
    #Escreva "Digite o salario"
    #Leia salario

# Se sal <= 1900 Então
# imposto = 0

#Senão
    #Se sal <= 2800 Então
    # imposto = sal * 0.15 #15%

    #Senão
    # imposto = sal * 0.275 #27,5%
    #fim_se
#Fim_se