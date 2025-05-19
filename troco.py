preco_unitario = float(input("Preço unitário do produto: "))
qtde_comprada = int(input("Quantidade comprada: "))
dinheiro_recebido = float(input("Dinheiro recebido: "))

troco = dinheiro_recebido - (preco_unitario * qtde_comprada)

print(f"TROCO = {troco:.2f}")

