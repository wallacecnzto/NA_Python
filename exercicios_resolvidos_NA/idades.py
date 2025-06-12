print("Dados da primeira pessoa:")
nome = input()
idade = int(input("Idade: "))
print("Dados da segunda pessoa:")
nome2 = input()
idade2 = int(input("Idade: "))

media = (idade + idade2) / 2.0

print(f"A idade média de {nome} e {nome2} é de {media:.1f}")
