import math

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))

delta = math.pow(b, 2) - 4 * a * c

if delta < 0:
    print("Esta equacao nao possui raizes reais")
else:
    x1 = ((-b + math.sqrt(delta))) / (2 * a) # atencao na precedencia!
    x2 = ((-b - math.sqrt(delta))) / (2 * a) # atencao na precedencia!
    
    print(f"X1 = {x1:.4f}")
    print(f"X2 = {x2:.4f}")