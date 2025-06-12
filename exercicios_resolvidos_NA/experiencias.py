n = int(input("Quantos casos serao digitados: "))
qtd_cobaias = 0
tipo_de_cobaias = ""
total_coelhos = 0
total_ratos = 0
total_sapos = 0
total_cobaias = 0
perc_coelhos = 0.0
perc_ratos = 0.0
perc_sapos = 0.0

for i in range(10):
    qtd_cobaias = int(input("Quantidade de cobaias: "))
    tipo_de_cobaias = input("Tipo de cobaia: ")
    
    if tipo_de_cobaias == "C":
        total_coelhos += qtd_cobaias
    elif tipo_de_cobaias == "R":
        total_ratos += qtd_cobaias
    else:
        total_sapos += qtd_cobaias
    
    total_cobaias += qtd_cobaias

perc_coelhos = (total_coelhos / total_cobaias) * 100
perc_ratos = (total_ratos / total_cobaias) * 100
perc_sapos = (total_sapos / total_cobaias) * 100

print("RELATORIO FINAL: ")
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {perc_coelhos:.2f}")
print(f"Percentual de ratos: {perc_ratos:.2f}")
print(f"Percentual de sapos: {perc_sapos:.2f}")
