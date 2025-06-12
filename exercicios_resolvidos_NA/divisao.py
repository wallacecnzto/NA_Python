casos = int(input("Quantos casos voce vai digitar? "))

for i in range(casos):
    numerador = int(input("Entre com numerador: "))
    denominador = int(input("Entre com o denominador: "))
    
    if denominador == 0:
        print("DIVISAO IMPOSSIVEL")
    else:
        divisao = numerador / denominador
        print(f"DIVISAO = {divisao:.2f}")