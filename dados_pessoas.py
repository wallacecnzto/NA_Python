n = int(input("Quantas pessoas serao digitadas: "))
lista_alturas = [0 for x in range(n)]
lista_genero = [0 for x in range(n)]
menor_altura = 0
maior_altura = 0
media_altura_mulheres = 0
soma_altura_mulheres = 0
qtd_mulheres = 0
num_homens = 0

for i in range(n):
    print(f"Altura da {i + 1}º pessoa: ")
    lista_alturas[i] = float(input())
    print(f"Genero da {i + 1}º pessoa: ")
    lista_genero[i] = input()
    
menor_altura = lista_alturas[0]
maior_altura = lista_alturas[0]

for i in range(n):
    if lista_alturas[i] < menor_altura:
        menor_altura = lista_alturas[i]
    if lista_alturas[i] > maior_altura:
        maior_altura = lista_alturas[i]

for i in range(n):
    if lista_genero[i] == "M":
        num_homens += 1
    else:
        if lista_genero[i] == "F":
            soma_altura_mulheres += lista_alturas[i]
            qtd_mulheres += 1

media_altura_mulheres = soma_altura_mulheres / qtd_mulheres

print(f"Menor altura = {menor_altura:.2f}")
print(f"Maior altura = {maior_altura:.2f}")
print(f"Media das alturas das mulheres = {media_altura_mulheres:.2f}")
print(f"Numero de homens = {num_homens}")
        