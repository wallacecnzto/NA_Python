# Crie uma função que fala se um número é par um ímpar.
# Retorne se esse número é par ou ímpar.

def par_ou_impar(x):
    if x % 2 == 0:
        return "Par"
    return "Impar"

print(par_ou_impar(3))
