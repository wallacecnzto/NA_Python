n = int(input("Serao digitados quantos produtos? "))
produtos = [0 for x in range(n)]
precos_compras = [0 for x in range(n)]
precos_vendas = [0 for x in range(n)]
total_compra = 0
total_venda = 0
lucro_total = 0
lucro = 0
lucro_percentual = 0
abaixo = 0
entre = 0
acima = 0
preco_compra = 0
preco_venda = 0

for i in range(n):
    print(f"Produto {i + 1}:")
    produtos[i] = input("Nome: ")
    precos_compras[i] = float(input("Preco de compra: "))
    precos_vendas[i] = float(input("Preco de venda: "))

for i in range(n):
    preco_compra = precos_compras[i]
    preco_venda = precos_vendas[i]
    lucro = preco_venda - preco_compra
    lucro_percentual = ( lucro / preco_compra) * 100
    # formula universal => lucro_percentual = ((preco_venda - preco_custo) / preco_custo) * 100
    
    if lucro_percentual < 10:
        abaixo += 1
    elif lucro_percentual >= 10 and lucro_percentual <= 20:
        entre += 1
    else:
        acima += 1
        
    total_compra += precos_compras[i]
    total_venda += precos_vendas[i]
    lucro_total += lucro
    
print("RELATORIO:")
print(f"Lucro abaixo de 10%: {abaixo}")
print(f"Lucro entre 10% e 20%: {entre}")
print(f"Lucro acima de 20%: {acima}")
print(f"Valor total de compra: {total_compra:.2f}")
print(f"Valor total de venda: {total_venda:.2f}")
print(f"Lucro total: {lucro_total:.2f}")
