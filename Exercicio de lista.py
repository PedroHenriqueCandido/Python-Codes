# Lista de perguntas
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Variável para contar as respostas positivas
respostas_positivas = 0

# Fazendo as perguntas e contando as respostas "sim"
for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não): ").strip().lower()
    if resposta == "sim":
        respostas_positivas += 1

# Classificando a pessoa com base nas respostas
if respostas_positivas == 5:
    classificacao = "Assassino"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 2:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"

# Mostrando a classificação final
print(f"\nClassificação: {classificacao}")

