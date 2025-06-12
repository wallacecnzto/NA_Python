preco_unitario = float(input("Preço unitário do produto: "))
qtde_comprada = int(input("Quantidade comprada: "))
valor_recebido = float(input("Dinheiro recebido: "))

total_a_pagar = preco_unitario * qtde_comprada
troco = total_a_pagar - valor_recebido

if valor_recebido < total_a_pagar:
    print(f"DINHEIRO INSUFICIENTE. FALTAM {troco:.2f}")
else:
    print(f"TROCO = {troco:.2f} REAIS")