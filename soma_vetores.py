n = int(input("Quantos valores vai ter cada vetor? "))
lista_a = []
lista_b = []
lista_c = [0 for x in range(n)]

for i in range(n):
    lista_a.append(int(input("Digite os valores do vetor A: ")))
    
for i in range(n):
    lista_b.append(int(input("Digite os valores do vetor B: ")))

for i in range(n):
    lista_c[i] = lista_a[i] + lista_b[i]

print("VETOR RESULTANTE:")

for i in range(n):
    print(lista_c[i])
