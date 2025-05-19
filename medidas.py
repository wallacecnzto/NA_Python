A = float(input("Digite a medida de A: "))
B = float(input("Digite a medida de B: "))
C = float(input("Digite a medida de C: "))

area_do_quadrado = A * A
area_do_triangulo = (B * A) / 2
area_do_trapezio = (A + B) * (C / 2)

print(f"AREA DO QUADRADO = {area_do_quadrado:.4f}")
print(f"AREA DO TRIANGULO = {area_do_triangulo:.4f}")
print(f"AREA DO TRAPEZIO = {area_do_trapezio:.4f}")
