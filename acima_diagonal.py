n = int(input("Qual a ordem da matriz? "))
matriz = [[0 for x in range(n)] for x in range(n)]
soma = 0

for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"Elemento [{i},{j}]: "))

for i in range(n):
    for j in range(n):
        if i < j: # A dica é comparar i com j!
            soma += matriz[i][j]

print(f"SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {soma}")
