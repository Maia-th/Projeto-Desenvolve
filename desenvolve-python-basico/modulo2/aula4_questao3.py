nomeProd1= input("\033[3mDigite o nome do produto 1: \033[0m")
precoProd1= float(input("\033[3mDigite o preço unitário do produto 1: \033[0m"))
qtdProd1=int(input("\033[3mDigite a quantidade do produto 1: \033[0m"))

nomeProd2= input("\033[3mDigite o nome do produto 2: \033[0m")
precoProd2= float(input("\033[3mDigite o preço unitário do produto 2: \033[0m"))
qtdProd2=int(input("\033[3mDigite a quantidade do produto 2: \033[0m"))

nomeProd3= input("\033[3mDigite o nome do produto 3: \033[0m")
precoProd3= float(input("\033[3mDigite o preço unitário do produto 3: \033[0m"))
qtdProd3=int(input("\033[3mDigite a quantidade do produto 3: \033[0m"))

print(f'Total: R${(precoProd1*qtdProd1)+(precoProd2*qtdProd2)+(precoProd3*qtdProd3):,.2f}')