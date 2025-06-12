# Crie uma função que multiplica todos os elementos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.

def multiplicar(*args):
    total = 1
    for i in args:
        total *= i
    return total

multiplicacao = multiplicar(1, 2, 3)

print(multiplicacao)