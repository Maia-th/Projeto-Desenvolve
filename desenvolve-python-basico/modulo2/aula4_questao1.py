#Entrada dos dados

comprimento = int(input("Digite o comprimento do terreno: "))
largura = int(input("Digite o largura do terreno: "))
precoMetro = float(input("Digite o preço do metro quadrado: "))

#Calculo da area

area = comprimento * largura

#Calculo do preço

precoTotal = area * precoMetro

#Imprensão

print(f'O terreno possui {area}m2 e custa R${precoTotal:,.2f}')