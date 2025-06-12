n = int(input("Quantos numeros voce vai digitar? "))
lista = []
soma = 0
media = 0

for i in range(n):
    lista.append(float(input("Digite um numero: ")))
    
for i in lista:
    soma += i

print()

media = soma / len(lista)

print("\nVALORES = ", end="")

for i in range(n):
	print(f"{lista[i]:.1f}  ", end="")

print(f"\nSOMA = {soma:.2f}")
print(f"MEDIA = {media:.2f}")
