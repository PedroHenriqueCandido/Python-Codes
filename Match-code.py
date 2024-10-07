n = -1
while n != 0:
    n = int(input("Digite um inteiro: "))
    match n:
        case 1:
            print(" voce digitou um ")
        case 2:
            print(" voce digitou dois ")
        case 3:
            print(" voce digitou tres ")
        case _:
            print(" voce digitou outra coisa ")
print("\n\nFim do programa")