# Dado um número pelo usuário, calcular e exibir os dez primeiros múltiplos deste número.
# Take input from the user
num = int(input("Enter a number: "))

# Initialize a counter
count = 0

# Calculate multiples until the 10th multiple is reached
while count < 10:
    # Calculate the next multiple
    multiple = num * (count + 1)

    # Print the multiple
    print(multiple)

    # Increment the counter
    count += 1