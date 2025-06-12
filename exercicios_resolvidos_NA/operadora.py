minutos = int(input("Digite a quantidade de minutos: "))
FRANQUIA = 100
VALOR_DA_FRANQUIA = 50.00
VALOR_EXCEDENTE = 2.00
total_a_pagar = (minutos - FRANQUIA) * VALOR_EXCEDENTE

if minutos <= 100:
    print(f"Valor a pagar: R$ {VALOR_DA_FRANQUIA:.2f}")
else:
    print(f"Valor a pagar: R$ {VALOR_DA_FRANQUIA + total_a_pagar:.2f}")