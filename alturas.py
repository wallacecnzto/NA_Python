n = int(input("Quantas pessoas serao digitadas? "))
lista = []
nome = ""
idade = 0
altura = 0
altura_media = 0
menores_de_dezesseis = 0
soma_alturas = 0
lista_menores = []

for i in range(n):
    print(f"Dados da {i + 1}a pessoa:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    
    if idade < 16:
        lista_menores.append(nome)
        menores_de_dezesseis += 1
        
    soma_alturas += altura
    
print()

altura_media = soma_alturas / n
menores = (menores_de_dezesseis / n) * 100

print(f"Altura media: {altura_media:.2f}")
print(f"Pessoas com menos de 16 anos: {menores:.1f}%")

for i in lista_menores:
    print(i, end="\n")
    