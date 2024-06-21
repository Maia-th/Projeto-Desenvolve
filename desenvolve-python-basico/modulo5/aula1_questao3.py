import random

numeroAleatorio = random.randint(1, 10)

while True:
    entradaUsuario = int(input("Adivinhe o número entre 1 e 10: "))
    
    if entradaUsuario == numeroAleatorio:
        print("Parabens, voce acertou!")
        break
    elif entradaUsuario < numeroAleatorio:
        print("Muito baixo, digite outro numero: ")
    else:
        print("Muito alto, digite outro numero:")