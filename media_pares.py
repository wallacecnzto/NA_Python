n = int(input("Quantos elementos vai ter o vetor? "))
lista = [0 for x in range(n)]
total_dos_pares = 0
qtd_num_pares = 0
media = 0
impar = 0

for i in range(n):
    lista[i] = int(input("Digite um numero: "))


for i in range(n):
    if lista[i] % 2 != 0:
        impar += 1
        
if impar == 0:
    print("NENHUM NUMERO PAR")
else:
    lista[i] % 2 == 0
    total_dos_pares += lista[i]
    qtd_num_pares += 1

    media = total_dos_pares / qtd_num_pares

    print(f"MEDIA DOS PARES = {media:.1f}")