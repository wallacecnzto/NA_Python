alcool = 0
gasolina = 0
diesel = 0

print("Informe um codigo (1, 2, 3) ou 4 para parar: ")

codigo = int(input())

while codigo != 4:
    
    if codigo == 1:
        alcool += 1
    elif codigo == 2:
        gasolina += 1
    elif codigo == 3:
        diesel += 1
        
    print("Informe um codigo (1, 2, 3) ou 4 para parar: ")
    codigo = int(input())

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
