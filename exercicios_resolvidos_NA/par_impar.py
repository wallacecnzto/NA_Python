N = int(input("Quantos numeros voce vai digitar? "))

for i in range(N):
    numero = int(input("Digite um numero: "))
    if numero == 0:
        print("NULO")
    elif numero % 2 == 0 and numero > 0:
        print("PAR POSITIVO")
    elif numero % 2 == 0 and numero < 0:
        print("PAR NEGATIVO")
    elif numero % 2 == 1 and numero > 0:
        print("IMPAR POSITIVO")
    else:
        print("IMPAR NEGATIVO")
    
"""

n: int; valor: int

n = int(input("Quantos numeros voce vai digitar? "))

for i in range(n):
	valor = int(input("Digite um numero: "))

	if valor == 0:
		print("NULO")
	else:
		if valor % 2 == 0:
			print("PAR", end="")
		else:
			print("IMPAR", end="")
		if valor > 0:
			print(" POSITIVO")
		else:
			print(" NEGATIVO")
""" 