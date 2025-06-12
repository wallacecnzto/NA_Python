valor = int(input("Deseja a tabuada para qual valor? "))

for i in range(1, 11):
    resultado = i * valor
    print(f"{valor} x {i} = {resultado}")
