n = int(input("Quantos numeros voce vai digitar? "))
lista = []
num_impar = []

for i in range(n):
    numero = int(input("Digite um numero: "))
    lista.append(numero)
    
for intem in lista:
    if intem < 0:
        num_impar.append(intem)

print("NUMEROS NEGATIVOS:")

for i in num_impar:
    print(i)

"""
n: int

n = int(input("Quantos numeros voce vai digitar? "))

vetor: [int] = [0 for x in range(n)]

for i in range(n):
	vetor[i] = int(input("Digite um numero: "))

print("NUMEROS NEGATIVOS:")

for i in range(n):
	if vetor[i] < 0:
		print(vetor[i])
"""