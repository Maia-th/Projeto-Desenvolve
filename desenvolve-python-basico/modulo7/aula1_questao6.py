from itertools import permutations

# Solicita ao usuário que digite uma frase
frase = input("Digite uma frase: ")

palavra_objetivo = input("Digite a palavra objetivo: ")

permutacoes = [''.join(p) for p in permutations(palavra_objetivo)]

anagramas = []

for permutacao in permutacoes:
    if permutacao.lower() in frase.lower():
        anagramas.append(permutacao)

print("Anagramas:", anagramas)
