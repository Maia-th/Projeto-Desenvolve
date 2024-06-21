def data_por_extenso(data):
    meses = {
        "01": "Janeiro",
        "02": "Fevereiro",
        "03": "Março",
        "04": "Abril",
        "05": "Maio",
        "06": "Junho",
        "07": "Julho",
        "08": "Agosto",
        "09": "Setembro",
        "10": "Outubro",
        "11": "Novembro",
        "12": "Dezembro"
    }
    
    dia, mes, ano = data.split("/")
    
    return f"{dia} de {meses[mes]} de {ano}"

data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

print("Você nasceu em", data_por_extenso(data_nascimento))
