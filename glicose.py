media = float(input("Digite a medida da glicose: "))

if media <= 100:
    print("Classificacao: normal")
elif media > 100 and media <= 140:
    print("Classificacao: elevado")
else:
    print("Classificacao: diabetes")