print("Digite dois numeros: ")
x = int(input())
y =  int(input())

if x > y:
    troca = x
    x = y
    y = troca
    
soma = 0

for numero in range(x + 1, y):
    if numero % 2 != 0:
        soma += numero
print(f"SOMA DOS IMPARES = {soma}")
