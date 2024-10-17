def converter_horario(hora, minuto):
    # Variável para armazenar AM ou PM
    if hora == 0:
        nova_hora = 12
        periodo = 'A'  # A.M.
    elif hora == 12:
        nova_hora = 12
        periodo = 'P'  # P.M.
    elif hora > 12:
        nova_hora = hora - 12
        periodo = 'P'  # P.M.
    else:
        nova_hora = hora
        periodo = 'A'  # A.M.
    
    return nova_hora, minuto, periodo

def exibir_horario(hora, minuto, periodo):
    # Formatar o minuto para ter dois dígitos
    minuto_formatado = f"{minuto:02d}"
    # Determinar se é AM ou PM
    sufixo = "A.M." if periodo == 'A' else "P.M."
    # Exibir o horário formatado
    print(f"{hora}:{minuto_formatado} {sufixo}")

def main():
    while True:
        # Entrada do usuário
        hora_24 = int(input("Informe a hora (formato 24 horas): "))
        minuto_24 = int(input("Informe o minuto: "))
        
        # Converter o horário
        hora_12, minuto, periodo = converter_horario(hora_24, minuto_24)
        
        # Exibir o horário convertido
        exibir_horario(hora_12, minuto, periodo)
        
        # Perguntar se o usuário deseja fazer outra conversão
        repetir = input("Deseja converter outro horário? (S/N): ").upper()
        if repetir != 'S':
            break

# Executar o programa
main()
