def desenhar_moldura(linhas=1, colunas=1):
    # Garantir que o número de linhas e colunas esteja dentro da faixa permitida (1 a 20)
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    # Desenhar a linha superior
    print('+' + '−' * (colunas - 2) + '+')
    
    # Desenhar as linhas do meio
    for _ in range(linhas - 2):
        print('|' + ' ' * (colunas - 2) + '|')
    
    # Desenhar a linha inferior
    if linhas > 1:  # Evitar duplicar a linha para o caso de linhas = 1
        print('+' + '−' * (colunas - 2) + '+')

# Solicitar ao usuário o número de linhas e colunas
linhas = int(input("Informe o número de linhas (1 a 20): "))
colunas = int(input("Informe o número de colunas (1 a 20): "))

# Chamar a função para desenhar a moldura
desenhar_moldura(linhas, colunas)
