duracao = int(input("Digite a duracao em segundos: "))

# 1 min = 60 seg
# 1 hora = 60 min ou 60 * 60 = 3600 seg

horas = duracao // 3600
resto = duracao % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas}:{minutos}:{segundos}")