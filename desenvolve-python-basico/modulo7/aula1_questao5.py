frase = input("Digite uma frase: ")

indices_vogais = []

contador_vogais = 0

for indice, caractere in enumerate(frase):
    if caractere.lower() in "aeiou":
        contador_vogais += 1
        indices_vogais.append(indice)

print(f"{contador_vogais} vogais")

print("Índices", indices_vogais)