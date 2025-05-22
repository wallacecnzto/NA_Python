print("Digite as idades: ")
idade = int(input())
contador = 0
soma = 0
media = 0

if idade < 0:
    print("IMPOSSIVEL CALCULAR")
   
while idade >= 0:
    soma += idade
    contador += 1
    idade = int(input())
    
    media = soma / contador
    
print(f"MEDIA = {media:.2f}")