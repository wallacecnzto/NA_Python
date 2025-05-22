print("Digite a primeira nota: ")
primeira_nota = float(input())

while primeira_nota < 0 or primeira_nota > 10.0:
    print("Valor invalido! Tente novamente: ")
    primeira_nota = float(input())

print("Digite a segunda nota: ")
segunda_nota = float(input())

while segunda_nota < 0 or segunda_nota > 10.0:
        print("Valor invalido! Tente novamente: ")
        segunda_nota = float(input())

media = 0

media = (primeira_nota + segunda_nota) / 2
    
print(f"MEDIA = {media:.2f}")
