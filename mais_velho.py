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
    
print(lista_nome)
print(lista_idade)
    
for i, j in zip(lista_idade, lista_nome):
    if i > idade:
        idade = i
        pessoa_mais_velha = j

print(f"PESSOA MAIS VELHA: {pessoa_mais_velha}")