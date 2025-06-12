largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
valor = float(input("Digite o valor do metro quadrado: "))

area_do_terreno = largura * comprimento
preco_do_terreno = valor * area_do_terreno

print(f"Area do terreno: {area_do_terreno:.2f}")
print(f"Preco do terreno: {preco_do_terreno:.2f}")
