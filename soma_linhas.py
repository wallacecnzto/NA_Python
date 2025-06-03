m_linhas = int(input("Qual a quantidade de linhas da matriz? "))
n_colunas = int(input("Qual a quantidade de colunas da matriz? "))
matriz = [[0 for x in range(n_colunas)] for x in range(m_linhas)]
vetor_gerado_de_soma = [0 for x in range(m_linhas)]

for i in range(m_linhas):
    print(f"Digite os elementos da {i + 1}º linha: ")
    for j in range(n_colunas):
        matriz[i][j] = float(input())

for i in range(m_linhas):
    soma_linhas = 0
    for j in range(n_colunas):
        soma_linhas += matriz[i][j]
    vetor_gerado_de_soma[i] = soma_linhas
    
print("VETOR GERADO:")

for i in range(m_linhas):
    print(f"{vetor_gerado_de_soma[i]:.1f}")
