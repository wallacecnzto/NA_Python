n = int(input("Quantos numeros voce vai digitar? "))
valor = 0
lista = []
maior_valor = 0
pos_maior_valor = 0

for i in range(n):
    valor = float(input("Digite um numero: "))
    if valor > maior_valor:
        maior_valor = valor
        pos_maior_valor = i

print()        
print(f"MAIOR VALOR = {maior_valor}")
print(f"POSICAO DO MAIOR VALOR = {pos_maior_valor}")