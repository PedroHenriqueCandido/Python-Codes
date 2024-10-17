def reverter_numero(numero):
    # Converter o número para string, reverter a string e depois converter de volta para inteiro
    numero_reverso = int(str(numero)[::-1])
    return numero_reverso

# Solicitar um número ao usuário
numero = int(input("Informe um número inteiro: "))

# Chamar a função e exibir o resultado
resultado = reverter_numero(numero)
print(f"O reverso de {numero} é {resultado}")
