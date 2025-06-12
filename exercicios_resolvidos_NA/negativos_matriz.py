m_linhas = int(input("Qual a quantidade de linhas da matriz? "))
n_colunas = int(input("Qual a quantidade de colunas da matriz? "))
matriz = [[0 for x in range(n_colunas)] for x in range(m_linhas)]

for i in range(m_linhas):
    for j in range(n_colunas):
        matriz[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("VALORES NEGATIVOS:")

for i in range(m_linhas):
    for j in range(n_colunas):
        if matriz[i][j] < 0:
            print(matriz[i][j])
