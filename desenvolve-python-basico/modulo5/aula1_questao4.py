from datetime import datetime

dataHhoraAtual = datetime.now()

dataFormatada = dataHhoraAtual.strftime("%d/%m/%Y")
horaFormatada = dataHhoraAtual.strftime("%H:%M")

print(f"Data: {dataFormatada}")
print(f"Hora:{horaFormatada}")