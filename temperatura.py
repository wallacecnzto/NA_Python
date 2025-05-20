escala = input("Voce vai digitar a temperatura em qual escala (C/F)? ")

if escala == "F":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    # formula C = 5/9 * (F - 32) 
    celsius = (5 / 9) * (fahrenheit - 32)
    print(f"Temperatura equivalente em Celsius: {celsius:.2f}")
else:
    escala == "C"
    celsius = float(input("Digite a temperatura equivalente em Celsius: "))
    # formula F = (°C * 9/5) + 32
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"Temperatura equivalente em Fahrenheit: {fahrenheit:.2f}")
    