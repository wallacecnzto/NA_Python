n = int(input("Qual a ordem da matriz? "))
mat = [[0 for x in range(n)] for x in range(n)]
cont = 0

for i in range(n):
    for j in range(n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))
    
print("DIAGONAL PRINCIPAL:")    
for i in range(n):
    print(f"{mat[i][i]} ", end="")
    
print()

for i in range(n):
    for j in range(n):
        if mat[i][j] < 0:
            cont += 1

print(f"QUANTIDADE DE NEGATIVOS = {cont}")