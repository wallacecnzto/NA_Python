n = int(input("Quantas pessoas voce vai digitar? "))
lista_nome = [0 for x in range(n)]
lista_idade = [0 for x in range(n)]
nome = ""
idade = 0
pessoa_mais_velha = ""

for i in range(n):
    print(f"Dados da {i + 1} pessoa:")
    lista_nome[i] = input("Nome: ")
    lista_idade[i] = int(input("Idade: "))
    
for i, j in zip(lista_idade, lista_nome):
    if i > idade:
        idade = i
        pessoa_mais_velha = j

print(f"PESSOA MAIS VELHA: {pessoa_mais_velha}")

"""
    n: int; maioridade: int; posicaomaior: int

n = int(input("Quantas pessoas voce vai digitar? "))

nomes: [str] = [0 for x in range(n)]
idades: [int] = [0 for x in range(n)]

for i in range(n):
	print(f"Dados da {i+1}a pessoa:")
	nomes[i] = str(input("Nome: "))
	idades[i] = int(input("Idade: "))

maioridade = idades[0]
posicaomaior = 0

for i in range(n):
	if idades[i] > maioridade:
		maioridade = idades[i]
		posicaomaior = i

print(f"PESSOA MAIS VELHA: {nomes[posicaomaior]}")
"""