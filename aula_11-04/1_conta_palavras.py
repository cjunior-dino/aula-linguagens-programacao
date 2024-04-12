texto = input("Digite um texto: ")

numero_de_palavras = 1

for letra in texto:
    if letra == " ":
        numero_de_palavras += 1

if texto[-1] == " ":
    numero_de_palavras -= 1

print(f"O número de palavras é: {numero_de_palavras}")
