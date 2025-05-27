n = int(input("Quantos casos voce vai digitar? "))

for i in range(n):
    print("Digite tres numeros: ")
    valor1 = float(input())
    valor2 = float(input())
    valor3 = float(input())
    
    PESO_DO_PRIMEIRO_VALOR = 2
    PESO_DO_SEGUNDO_VALOR = 3
    PESO_DO_TERCEIRO_VALOR = 5
    SOMA_DOS_PESOS = PESO_DO_PRIMEIRO_VALOR + PESO_DO_SEGUNDO_VALOR + PESO_DO_TERCEIRO_VALOR
    
    media_poderada = ((valor1 * PESO_DO_PRIMEIRO_VALOR) + (valor2 * PESO_DO_SEGUNDO_VALOR) + (valor3 * PESO_DO_TERCEIRO_VALOR)) / SOMA_DOS_PESOS
    print(f"MEDIA = {media_poderada:.1f}")