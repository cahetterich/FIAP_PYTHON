print ("Digite 3 números: ")
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2:
    maior = n1
elif n1 < n2:
    maior = n2
elif n2 > n3:
     maior = n3
elif n2 < n3:
     maior = n2
elif n1 > n3:
     maior = n1
else:
    maior = n3
print("Maior número: ", maior)

print ("Digite 3 números: ")
n01 = int(input())
n02 = int(input())
n03 = int(input())
maior = n01
if n02 > maior:
    maior = n01
if n03 > maior:
    maior = n03
print ("Maior número: ", maior)