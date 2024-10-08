numero_escolhido = int(input("Digite um número de 0 a 10: "))
while numero_escolhido < 0 or numero_escolhido > 10:
    numero_escolhido = int(input("Número inválido, digite um número de 0 a 10: "))
print("Parabéns, você consegue digitar um número de 0 a 10!")
