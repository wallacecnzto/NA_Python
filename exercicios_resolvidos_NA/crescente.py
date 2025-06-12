print("Digite dois numeros: ")
num1 = int(input())
num2 = int(input())

while num1 != num2:
    if num1 > num2:
        print(f"DECRESCENTE!")        
    else:
        print(f"CRESCENTE!")
    
    print("Digite outros dois numeros: ")
    num1 = input()
    num2 = input()
