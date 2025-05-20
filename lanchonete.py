COD1 = 5.00
COD2 = 3.50
COD3 = 4.80
COD4 = 8.90
COD5 = 7.32

codigo = float(input("Codigo do produto comprado: "))
qtde_comprada = int(input("Quantidade comprada: "))

if codigo == 1:
    valor_a_pagar = COD1 * qtde_comprada
    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
elif codigo == 2:
    valor_a_pagar = COD2 * qtde_comprada
    print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
elif codigo == 3:
    valor_a_pagar = COD3 * qtde_comprada
    print(f"Valor a pagar R$ {valor_a_pagar:.2f}")
elif codigo == 4:
    valor_a_pagar = COD4 * qtde_comprada
    print(f"Valor a pagar R$ {valor_a_pagar:.2f}")
else:
    valor_a_pagar = COD5 * qtde_comprada
    print(f"Valor a pagar R$ {valor_a_pagar:.2f}")

               