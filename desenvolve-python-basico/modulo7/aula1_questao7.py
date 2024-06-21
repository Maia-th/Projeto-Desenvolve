import random

def encrypt(nomes):
    chave_aleatoria = random.randint(1, 10)

    nomes_cript = []

    for nome in nomes:
        nome_criptografado = ""

        for char in nome:
            if ord(char) >= 33 and ord(char) <= 126:
                novo_char = chr((ord(char) - 33 + chave_aleatoria) % 94 + 33)
                nome_criptografado += novo_char
            else:
                nome_criptografado += char

        nomes_cript.append(nome_criptografado)
    
    return nomes_cript, chave_aleatoria