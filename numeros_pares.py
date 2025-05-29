n = int(input("Quantos numeros voce vai digitar? "))
num = 0
lista_de_pares = []
qtd_pares = 0
lista = []

for i in range(n):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        lista_de_pares.append(num)
        qtd_pares += 1
        
print()

print("QUANTIDADE DE PARES: ")

for i in lista_de_pares:
    print(i, end=" ")
    
print()

print(f"\nQuantidade de pares = {qtd_pares}")