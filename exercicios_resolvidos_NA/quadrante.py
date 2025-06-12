print("Digite o valor das coordenadas de X e Y: ")
x = int(input())
y = int(input())

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print("QUADRANTE Q1")
    elif x > 0 and y < 0:
        print("QUADRANTE Q4")
    elif x < 0 and y < 0:
        print("QUADRANTE Q3")
    elif x < 0 and y > 0:
        print("QUADRANTE Q2")
    
    print("Digite os valores das coordenadas de X e Y: ")
    x = int(input())
    y = int(input())
