def substituir_vogais_por_asterisco(frase):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    for vogal in vogais:
        frase = frase.replace(vogal, "*")
    
    return frase

frase_original = input("Digite uma frase: ")

frase_modificada = substituir_vogais_por_asterisco(frase_original)

print("Frase modificada:", frase_modificada)