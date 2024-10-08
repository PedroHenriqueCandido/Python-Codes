# Lê um número inteiro n do usuário
n = int(input("Digite um número inteiro: "))

# Loop de 1 até n
for i in range(1, n + 1):
    # Imprime os números de 1 até i, separados por espaço
    for j in range(1, i + 1):
        print(j, end=' ')
    print()  # Para pular para a próxima linha
