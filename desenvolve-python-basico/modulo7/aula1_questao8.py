def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")
    soma = 0

    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    if int(cpf[9]) != digito_verificador_1:
        return False
    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    if int(cpf[10]) != digito_verificador_2:
        return False
    
    return True

cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")
if validar_cpf(cpf):
    print("CPF válido")
else:
    print("CPF inválido")