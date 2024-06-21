import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

max_negativos = 0
intervalo_inicio = 0
intervalo_fim = 0

for i in range(len(lista)):
    for j in range(i+1, len(lista)+1):
        sublista = lista[i:j]
        negativos = sum(1 for x in sublista if x < 0)
        if negativos > max_negativos:
            max_negativos = negativos
            intervalo_inicio, intervalo_fim = i, j

del lista[intervalo_inicio:intervalo_fim]

print("Editada:", lista)
