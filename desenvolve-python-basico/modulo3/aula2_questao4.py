classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
pforca = int(input("Digite os pontos de força (de 1 a 20): "))
pmagia = int(input("Digite os pontos de magia (de 1 a 20): "))

if classe == "guerreiro":
    if pforca >=15 and pmagia <= 10:
        print("Pontos de atributo consistentes com a classe escolhida: True")
    else:
        print("Pontos de atributo consistentes com a classe escolhida: False")
elif classe == "mago":
    if pforca <= 10 and pmagia >= 15:
        print("Pontos de atributo consistentes com a classe escolhida: True")
    else:
        print("Pontos de atributo consistentes com a classe escolhida: False")
else:
    if (pforca > 5 and pforca <= 15) and (pmagia> 5 and pmagia <= 15):
        print("Pontos de atributo consistentes com a classe escolhida: True")
    else:
        print("Pontos de atributo consistentes com a classe escolhida: False")