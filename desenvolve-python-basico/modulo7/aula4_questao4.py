import random

def ler_palavras():
    try:
        with open("gabarito_forca.txt", "r") as arquivo:
            palavras = arquivo.read().splitlines()
        return palavras
    except FileNotFoundError:
        print("Arquivo 'gabarito_forca.txt' não encontrado.")
        return []

def ler_estagios_enforcado():
    try:
        with open("gabarito_enforcado.txt", "r") as arquivo:
            estagios_enforcado = arquivo.read().strip().split("\n\n")
        return estagios_enforcado
    except FileNotFoundError:
        print("Arquivo 'gabarito_enforcado.txt' não encontrado.")
        return []

def exibir_palavra_oculta(palavra, letras_corretas):
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra + " "
        else:
            palavra_oculta += "_ "
    return palavra_oculta.strip()


def imprime_enforcado(estagios_enforcado,erros):
    if erros > len(estagios_enforcado) - 1:
        erros = len(estagios_enforcado) - 1  

    print(estagios_enforcado[erros])

def jogar_forca():
    palavras = ler_palavras()
    if not palavras:
        return

    palavra_sorteada = random.choice(palavras).upper()
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6
    erros = 0

    estagios_enforcado = ler_estagios_enforcado()
    if not estagios_enforcado:
        return

    print("Bem-vindo ao jogo da Forca!")
    print("Adivinhe a palavra secreta.")
    print(exibir_palavra_oculta(palavra_sorteada, letras_corretas))

    while True:
        if all(letra in letras_corretas for letra in palavra_sorteada):
            print("Parabéns! Você acertou a palavra!")
            break

        if erros >= tentativas:
            print("Você perdeu! A palavra era:", palavra_sorteada)
            break

        letra = input("Digite uma letra: ").strip().upper()

        if len(letra) != 1 or not letra.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou esta letra. Tente outra.")
            continue

        if letra in palavra_sorteada:
            letras_corretas.add(letra)
            print("Letra correta!")
            print(exibir_palavra_oculta(palavra_sorteada, letras_corretas))
        else:
            letras_erradas.add(letra)
            erros += 1
            print("Letra errada!")
            imprime_enforcado(estagios_enforcado,erros)
            print(exibir_palavra_oculta(palavra_sorteada, letras_corretas))

if __name__ == "__main__":
    jogar_forca()
