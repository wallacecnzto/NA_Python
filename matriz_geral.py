n = int(input("Qual a ordem da matriz? "))
matriz = [[0 for x in range(n)] for x in range(n)]
soma_dos_positivos = 0
matriz_alterada = [[0 for x in range(n)] for x in range(n)]


for i in range(n):
    for j in range(n):
        matriz[i][j] = float(input(f"Elemento [{i},{j}]: "))

for i in range(n):
    for j in range(n):
        if matriz[i][j] >= 0:
            soma_dos_positivos += matriz[i][j]

print()

print(f"SOMA DOS POSITIVOS: {soma_dos_positivos:.1f}")

print()

linha_escolhida = int(input("Escolha uma linha: "))

print("LINHA ESCOLHIDA: ", end="")
for i in range(n):
    print(f"{matriz[linha_escolhida][i]:.1f}", end=" ")
 
print()
print()
       
coluna_escolhida = int(input("Escolha uma coluna: ")) # A dica é aproveitar essa variável na matriz!

print("COLUNA ESCOLHIDA: ", end="")
for i in range(n):
    print(f"{matriz[i][coluna_escolhida]:.1f}", end=" ")
        
print()
print()

print("DIAGONAL PRINCIPAL: ", end="")
for i in range(n):
    print(matriz[i][i], end=" ")
    
print()
print()

for i in range(n):
    for j in range(n):
        if matriz[i][j] < 0:
            matriz[i][j] *= matriz[i][j]

print("MATRIZ ALTERADA:")
for i in range(n):
    for j in range(n):
        print(matriz[i][j], end=" ")
    print()