m_linhas = int(input("Quantas linhas vai ter cada matriz? "))
n_colunas = int(input("Quantas colunas vai ter cada matriz? "))
matriz_A = [[0 for x in range(n_colunas)] for x in range(m_linhas)]
matriz_B = [[0 for x in range(n_colunas)] for x in range(m_linhas)]
matriz_C = [[0 for x in range(n_colunas)] for x in range(m_linhas)]

for i in range(m_linhas):
    for j in range(n_colunas):
        print("Digite os valore da matriz A:")
        matriz_A[i][j] = int(input(f"Elemento [{i},{j}]: "))

for i in range(m_linhas):
    for j in range(n_colunas):
        print("Digite os valore da matriz B:")
        matriz_B[i][j] = int(input(f"Elemento [{i},{j}]: "))

for i in range(m_linhas):
    for j in range(n_colunas):
        matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]

print("MATRIZ SOMA:")

for i in range(m_linhas):
    for j in range(n_colunas):
        print(f"{matriz_C[i][j]}", end=" ")
    print()