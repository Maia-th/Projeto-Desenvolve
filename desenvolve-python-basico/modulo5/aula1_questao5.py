import emoji

emojis_disponiveis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

print("Emojis disponíveis:")
for codigo, emoji_valor in emojis_disponiveis.items():
    print(f"{emoji_valor} - {codigo}")

frase = input("\nDigite uma frase e ela será emojizada: ")

for codigo, emoji_valor in emojis_disponiveis.items():
    frase = frase.replace(codigo, emoji_valor)

print("Frase emojizada:")
print(frase)