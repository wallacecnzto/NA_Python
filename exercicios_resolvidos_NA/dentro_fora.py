numeros = int(input("Quantos numeros voce vai digitar? "))
dentro = 0
fora = 0

for numero in range(numeros):
    i = int(input())
    if i in range(10, 20 + 1): # ou if x < 10 or x > 20 ? fora += 1 : dentro += 1 
        dentro += 1
    else:
        fora += 1
print(f"{dentro} DENTRO")
print(f"{fora} FORA")
