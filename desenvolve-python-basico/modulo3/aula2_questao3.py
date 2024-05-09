idade = int(input("Digite a sua idade: "))

if idade >= 16 and idade <= 18:
    vezesJogadas = int(input("Você já jogou pelo menos 3 jogos de tabuleiro ? Digite 1 para SIM ou 0 para Não!: "))
    if vezesJogadas:
        top1 = int(input("Quantas vezes você venceu um jogo?: "))
        if top1 >=1:
            print("True")
        else:
            print("False")
    else:
        print ("False")
else:
    print ("False")