sexo = input("Digite o seu gênero (M ou F): ")
idade = int(input("Digite a sua idade: "))
servico = int(input("Digite o seu tempo de serviço em anos: "))

if (sexo == "M" and idade > 65) or (sexo == "F" and idade > 60) or servico >= 30 or (idade >= 60 and servico >=25):
    print("True")
else:
    print ("False")
