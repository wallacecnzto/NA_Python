n = int(input("Quantos elementos vai ter no vetor? "))
lista = [0 for x in range(n)]
media = 0
soma = 0

for i in range(n):
    lista[i] = float(input("Digite um numero: "))
    
for i in range(n):
    soma += lista[i]
    
media = soma / n

print()

print(f"MEDIA DO VETOR = {media:.3f}")

print("ELEMENTOS ABAIXO DE MEDIA:")
for i in range(n):
    if lista[i] < media:
        print(lista[i])