qtd1 = int(input("\nDigite a quantidade de elementos da lista 1: "))
lista1 = []
lista2 = []

print(f"Digite os {qtd1} elementos da lista 1:")
for i in range(qtd1):
    item = int(input())
    lista1.append(item)


qtd2 = int(input("\nDigite a quantidade de elementos da lista 2: "))

print(f"Digite os {qtd2} elementos da lista 2:")
for i in range(qtd2):
    item = int(input())
    lista2.append(item)

lista3 = []

min_len = min(qtd1, qtd2)
for i in range(min_len):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

if qtd1 > qtd2:
    lista3.extend(lista1[min_len:])
else:
    lista3.extend(lista2[min_len:])

print("Lista intercalada:", ' '.join(map(str, lista3)))