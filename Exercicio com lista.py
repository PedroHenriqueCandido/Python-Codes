Codigos = [103, 117, 121, 135, 161, 189, 200, 204, 216]
Lista = []
print('Alternativa com if classico')
for codigo in Codigos:
    if 120 <= codigo and codigo <= 200:
        Lista.append(codigo)
print(f"Codigos filtrados -->  {Lista}")

Lista = []
print("\n\n Alternativa com if de unica linha")
for codigo in Codigos: 
    Lista.append(codigo) if 120 <= codigo and codigo<= 200 else 0
print(f"Codigos filtrados -->  {Lista}")